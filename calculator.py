# calculator

def main():
    while True:
        a = float(input("Введіть перше число або 'стоп' для завершення: "))
        b = float(input("Введіть друге число або 'стоп' для завершення: "))
        c = input("Введіть що хочете зробити (+, -, *, /), або 'стоп' для завершення: ")
        if c.lower() == "стоп":
            print("Робота завершена")
            break
        
        opreations = {
            "+" : a + b,
            "-" : a - b,
            "*" : a * b,
            "/" : a / b if b != 0 else "Ділення на нуль!"
        }
        
        result = opreations.get(c, "Невідома дія")
        print(result)
        
    
main()

