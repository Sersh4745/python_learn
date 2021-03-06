"""
    Алгоритм Эвклида. НОД - наибольший общий делитель

    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть
     НОД (следует выйти из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.
"""
a = int(input('a = '))
b = int(input('b = '))

while a != b:
    if a > b:
        if a % b == 0:
            print('Число НОД =', b)
            break
        else:
            print('Заменяем большее число на остаток от деления')
            a = a % b
            continue
    else:
        if b % a == 0:
            print('Число НОД =', a)
            break
        else:
            print('Заменяем большее число на остаток от деления')
            b = b % a
            continue
else:
    print('Введите не одинковые числа: ')
