try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    symbol = input("Введите операцию (+, -, *, /): ")

    if symbol == "+":
        print("Результат:", a + b)

    if symbol == "-":
        print("Результат:", a - b)

    if symbol == "*":
        print("Результат:", a * b)

    if symbol == "/":
        if b == 0:
            print("Ошибка: На ноль делить нельзя")
        else:
            print("Результат:", a / b)

    if symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/":
        print("Ошибка: Введите правильную операцию")

except ValueError:
    print("Ошибка: Введите только цифры")
