from fractions import Fraction
from datetime import datetime

def add():
    num1 = Fraction(input("Введите первое число: "))
    num2 = Fraction(input("Введите второе число: "))
    return num1 + num2

def subtract():
    num1 = Fraction(input("Введите уменьшаемое число: "))
    num2 = Fraction(input("Введите вычитаемое число: "))
    return num1 - num2

def multiply():
    num1 = Fraction(input("Введите первое число: "))
    num2 = Fraction(input("Введите второе число: "))
    return num1 * num2

def divide():
    num1 = Fraction(input("Введите делимое число: "))
    num2 = Fraction(input("Введите делитель: "))
    if num2 == 0:
        print("Ошибка: деление на ноль.")
        return 0
    return num1 / num2

def print_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Текущее время:", current_time)

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Текущее время")
    print("0. Выход")

    choice = input()

    if choice == '0':
        print("Программа завершена.")
        break

    try:
        if choice == '1':
            result = add()
        elif choice == '2':
            result = subtract()
        elif choice == '3':
            result = multiply()
        elif choice == '4':
            result = divide()
        elif choice == '5':
            print_current_time()
            continue
        else:
            print("Некорректный выбор операции. Повторите ввод.")
            continue

        print("Результат:", result)

    except ValueError:
        print("Некорректный ввод числа. Повторите ввод.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
