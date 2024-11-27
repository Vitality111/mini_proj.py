# # shoping list

# def main_shop():
#     shop_list = {}   
#     def shoping_list(): 
#         for i, (p, q) in enumerate(shop_list.items(), start=1):
#             print(f"{i}. {p}: {q}")
            
#     def del_list():
#         while True:
#             try:
                
                
#                 print ("\nВиберіть що хочете видалити за номером зі списку: ")
#                 shoping_list()
#                 del_prod = int(input("\n"))
                
                
#                 for i, (k,v) in enumerate(shop_list.items(), start=1):
#                     if del_prod == i:
#                         shop_list.pop(k,None)
#                         print ("Оновлений список:")
#                         shoping_list()
#                         break
#                 else:
#                     print("Такого номера немає")
#                     return
                
#                 confirmation = int(input("Якщо ви хочете видалити ще натисніть '1' якщо ні написніть '2': "))
#                 if confirmation == 1:
#                     continue
#                 elif confirmation == 2:
#                     return
#                 else:
#                     print("Невірно введені данні, повернення до основного меню")
#                     return
#             except ValueError:
#                 print("Будь ласка, введіть коректний номер.")
#             except Exception as e:
#                 print(f"Сталася помилка: {e}")

       
        
#     while True:
#         try:
#             product = input("\nВведіть продукт або 'Стоп': ")
#             if product.lower() == "стоп": 
#                 break
#             elif product.lower()  == "вид":
#                 del_list()
#                 continue
            
#             products_count = input("\nВведіть кількість або 'Стоп': ")
#             if products_count.lower() == "стоп":
#                 break
#             elif products_count.lower() == "вид":
#                 del_list()
#                 continue
            
#             if product and products_count:
#                 shop_list[product] = products_count
#                 print("\nВже у списку")
#                 shoping_list()
#                 print("\nЯкщо хочете щось видалити введіть 'Вид'")
#             else:
#                 print("Виникла помилка спрабуйте ще раз")
                
#         except Exception as e:
#             print(f"Помилка {e}")
    
#     print("\nВаш список покупок:")
#     shoping_list()       
    
    
# main_shop()
            
    
        # shoping list

# def main_shop():
#     shop_list = {}   
#     def shoping_list(): 
#         for i, (p, q) in enumerate(shop_list.items(), start=1):
#             print(f"{i}. {p}: {q}")
            
#     def del_list():
#         while shop_list:
#             shoping_list()
#             try:
#                 del_prod = int(input("\nВиберіть що хочете видалити за номером зі списку: "))
#                 k = list(shop_list.keys())[del_prod - 1]
#                 shop_list.pop(k)
#                 print(f"Продукт '{k}' видалено.")
#                 confirmation = input("Якщо ви хочете видалити ще натисніть '1', якщо ні - '2': ").strip()
#                 if confirmation == "1":
#                     continue
#                 elif confirmation == '2':
#                     break  # Виходимо з циклу, якщо не хочемо більше видаляти
#             except (ValueError, IndexError):
#                 print("Невірний номер. Спробуйте ще раз.")
                
                    
#     while True:
#         try:
#             product = input("\nВведіть продукт або 'Стоп': ")
#             if product.lower() == "стоп": 
#                 break
#             elif product.lower()  == "вид":
#                 del_list()
#                 continue
            
#             products_count = input("\nВведіть кількість або 'Стоп': ")
#             if products_count.lower() == "стоп":
#                 break
#             elif products_count.lower() == "вид":
#                 del_list()
#                 continue
            
#             if product and products_count:
#                 shop_list[product] = products_count
#                 print("\nВже у списку")
#                 shoping_list()
#                 print("\nЯкщо хочете щось видалити введіть 'Вид'")
#             else:
#                 print("Виникла помилка спрабуйте ще раз")
                
#         except Exception as e:
#             print(f"Помилка {e}")
    
#     print("\nВаш список покупок:")
#     shoping_list()    



import tkinter as tk
from tkinter import messagebox

# Функція для виведення списку покупок
def shoping_list():
    list_display.delete(1.0, tk.END)  # Очищаємо виведення перед оновленням
    for i, (p, q) in enumerate(shop_list.items(), start=1):
        list_display.insert(tk.END, f"{i}. {p}: {q}\n")

# Функція для додавання продукту в список
def add_product():
    product = product_entry.get()
    count = count_entry.get()
    
    if product.lower() == "стоп" or count.lower() == "стоп":
        window.quit()
        return
    
    if product and count:
        shop_list[product] = count
        product_entry.delete(0, tk.END)
        count_entry.delete(0, tk.END)
        shoping_list()
    else:
        messagebox.showerror("Помилка", "Будь ласка, введіть правильне значення.")

# Функція для видалення продукту зі списку
def del_product():
    try:
        del_prod = int(del_prod_entry.get())
        if 1 <= del_prod <= len(shop_list):
            k = list(shop_list.keys())[del_prod - 1]
            shop_list.pop(k)
            messagebox.showinfo("Успіх", f"Продукт '{k}' видалено.")
            del_prod_entry.delete(0, tk.END)
            shoping_list()
        else:
            messagebox.showerror("Помилка", "Невірний номер.")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректний номер.")
        
# Створення головного вікна
window = tk.Tk()
window.title("Список покупок")

# Словник для зберігання продуктів
shop_list = {}

# Інтерфейс для введення продукту та кількості
tk.Label(window, text="Введіть продукт:").pack()
product_entry = tk.Entry(window)
product_entry.pack()

tk.Label(window, text="Введіть кількість:").pack()
count_entry = tk.Entry(window)
count_entry.pack()

add_button = tk.Button(window, text="Додати продукт", command=add_product)
add_button.pack()

# Інтерфейс для видалення продукту
tk.Label(window, text="Введіть номер продукту для видалення:").pack()
del_prod_entry = tk.Entry(window)
del_prod_entry.pack()

del_button = tk.Button(window, text="Видалити продукт", command=del_product)
del_button.pack()

# Виведення списку покупок
list_display = tk.Text(window, height=10, width=30)
list_display.pack()

# Запуск інтерфейсу
shoping_list()
window.mainloop()
   
    
