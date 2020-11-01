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
            else :
                print(x / y)
        else:
            print('Не верный знак , повторите операцию.')
        
        c = str(input('Continue? (y/n): '))
        if  c == 'y':
            continue    
        else:
            break
    except:
        print('Введите число')
