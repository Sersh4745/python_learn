"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""

while True:
    try:
        x = int(input('x = '))
        y = int(input('y = '))
        operator = input('Знак: ')

        if operator == '+':
            print(x + y)
        elif operator == '-':
            print(x - y)
        elif operator == '*':
            print(x * y)
        elif operator == '/':
            if y == 0:
                print('На ноль дельнить нельзя!')
            else:
                print(x / y)
        else:
            print('Не верный знак , повторите операцию.')

        c = str(input('Continue? (y/n): '))
        if c == 'y':
            continue
        else:
            break
    except ValueError:
        print('Введите число')
