import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

response = requests.get(url)  # Завантажуємо HTML-код сторінки

# Перевіряємо, чи сторінка завантажилась успішно
if response.status_code == 200:  
    print("Сторінка успішно завантажена!")
    
    # Крок 3: Створюємо об'єкт BeautifulSoup для аналізу HTML
    soup = BeautifulSoup(response.text, 'html.parser')  
    
    # Крок 4: Шукаємо всі елементи <h2> на сторінці
    headers = soup.find_all("h2")  # Знаходимо всі теги <h2>
    
    # Виводимо кожен заголовок
    for idx, header in enumerate(headers, start=1):
        print(f"Заголовок {idx}: {header.text.strip()}")
else:
    print("Помилка при завантаженні сторінки, код:", response.status_code)