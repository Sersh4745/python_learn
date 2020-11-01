a = int(input('a = '))
b = int(input('b = '))

while a != b:
    if a > b:
        if  a % b == 0:
            print('Число НОД =',b)
            break
        else:
            print('Заменяем большее число на остаток от деления')
            a = a % b
            continue
    else:
        if  b % a == 0:
            print('Число НОД =',a)
            break
        else:
            print('Заменяем большее число на остаток от деления')
            b = b % a 
            continue
else:
        print('Введите не одинковые числа: ')
        

