import pyaudio
import numpy as np
import noisereduce as nr
import tkinter as tk
import threading
import time

# Параметри мікрофону
RATE = 44100  # Частота дискретизації
CHUNK = 1024  # Розмір блоку аудіо
SLEEP_TIME = 100  # Інтервал оновлення (мс)
NOISE_THRESHOLD = 1000  # Поріг шуму для активування шумопригнічення

# Ініціалізація PyAudio
p = pyaudio.PyAudio()

def get_audio():
    """Функція для отримання аудіо з мікрофону"""
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    return data

def reduce_noise(audio_data):
    """Функція для шумопригнічення"""
    reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE)
    return reduced_noise

def adjust_volume(audio_data, factor=1.0):
    """Функція для регулювання гучності"""
    return audio_data * factor

def process_audio():
    """Обробка аудіо: активує шумопригнічення, якщо рівень шуму перевищує поріг"""
    audio_data = get_audio()  # Отримуємо аудіо
    volume_factor = volume_slider.get()  # Отримуємо коефіцієнт гучності з слайдера
    adjusted_audio = adjust_volume(audio_data, volume_factor)  # Регулюємо гучність
    
    # Обчислюємо рівень шуму (середнє значення абсолютних амплітуд)
    noise_level = np.abs(adjusted_audio).mean()

    # Якщо рівень шуму перевищує поріг, застосовуємо шумопригнічення
    if noise_level > NOISE_THRESHOLD:
        reduced_audio = reduce_noise(adjusted_audio)  # Застосовуємо шумопригнічення
    else:
        reduced_audio = adjusted_audio  # Якщо шум низький, просто передаємо аудіо без змін

    # Оновлення рівня шуму на графічному інтерфейсі
    update_noise_bar(noise_level)
    
    # Оновлення кожні SLEEP_TIME мс
    window.after(SLEEP_TIME, process_audio)

def update_noise_bar(noise_level):
    """Оновлення рівня шуму на шкалі"""
    # Нормалізація рівня шуму до діапазону 0-100 (максимум 100%)
    normalized_level = min(noise_level / 3000, 1)  # 3000 - максимальний рівень шуму, який ми дозволяємо
    # Оновлення ширини бару
    noise_bar.config(width=int(normalized_level * 300))

# Створення графічного інтерфейсу
window = tk.Tk()
window.title("Мікрофон: шумопригнічення")
window.geometry("400x250")

# Лейбл для заголовка
title_label = tk.Label(window, text="Рівень шуму", font=("Arial", 14))
title_label.pack(pady=10)

# Полоска для рівня шуму
noise_bar_frame = tk.Frame(window, width=350, height=30, bg="gray")
noise_bar_frame.pack(pady=20)

# Полоска для рівня шуму (заповнюється кольором залежно від рівня)
noise_bar = tk.Label(noise_bar_frame, bg="green", height=2)
noise_bar.pack(fill=tk.Y)

# Слайдер для регулювання гучності
volume_slider = tk.Scale(window, from_=0, to_=2, resolution=0.1, orient='horizontal', label="Гучність")
volume_slider.set(1.0)  # Значення за замовчуванням 1 (нормальний рівень)
volume_slider.pack(pady=10)

# Запуск процесу аудіо обробки в окремому потоці
audio_thread = threading.Thread(target=process_audio, daemon=True)
audio_thread.start()

# Запуск інтерфейсу
window.mainloop()
