# calculator.py

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументи мають бути числами")
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Помилка: ділення на нуль")
    return a / b

def main():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print("Оберіть операцію: +, -, *, /")
        operation = input("Операція: ")
        if operation == "+":
            print("Результат:", add(a, b))
        elif operation == "-":
            print("Результат:", subtract(a, b))
        elif operation == "*":
            print("Результат:", multiply(a, b))
        elif operation == "/":
            print("Результат:", divide(a, b))
        else:
            print("Невідома операція")
    except ValueError as e:
        print("Помилка:", e)

if __name__ == "__main__":
    main()

