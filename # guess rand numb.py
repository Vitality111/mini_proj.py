# guess rand numb 

# import random


# def main():
#     numbers_for_game = int(input("Введіть до якого числа будете вгадувати? Відлік починається з 1: "))
#     number_for_game = random.randint(1 , numbers_for_game)
#     while True:
#         user_number = int(input(f"Вгадайте число від 1 до {numbers_for_game}: "))
#         if user_number == number_for_game:
#             print(f"Вірно, число {user_number}!! Ви вгадали")
#             break
#         else: print("Невірно, спробуйте ще")
# main()

import random


def main():
    numbers_for_game = int(input("Введіть до якого числа будете вгадувати? Відлік починається з 1: "))
    number_for_game = random.randint(1, numbers_for_game)  # Генерація числа для гри
    attempts = 0  # Лічильник спроб

    while True:
        try:
            user_number = int(input(f"Вгадайте число від 1 до {numbers_for_game}: "))  # Введення числа користувачем
            if user_number < 1 or user_number > numbers_for_game:
                print(f"Будь ласка, введіть число від 1 до {numbers_for_game}")
                continue  # Якщо число не в діапазоні, попросити повторити введення
        except ValueError:
            print("Введіть правильне число!")
            continue  # Якщо введено не число, повторити спробу

        attempts += 1  # Збільшити лічильник спроб

        if user_number == number_for_game:
            print(f"Вірно, число {user_number}!! Ви вгадали за {attempts} спроб.")
            break  # Вийти з гри
        else:
            print("Невірно, спробуйте ще")


main()
