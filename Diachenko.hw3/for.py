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
    except ValueError:
        print('Введите число: ')
        continue
    operator = input('Знак: ')
    r = None
    for _ in range(x):
        try:
            y = int(input('Введите число: '))
        except ValueError:
            print('Введите число: ')
            continue
        if r is None:
            r = y
        else:
            if operator == '+':
                r += y
            elif operator == '-':
                r -= y
            elif operator == '*':
                r *= y
            elif operator == '/':
                if y == 0:
                    print('На ноль дельнить нельзя!')
                    break
                else:
                    r /= y
            print(r)

    if input('Continue? (y/n) ') != 'y':
        break
