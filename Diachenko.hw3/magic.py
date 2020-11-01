print('Привет. Это программа "Магическое число"')
import random 
n = 0 #Кол попыток
Name = input('Введите свое имя: ')
random_number = random.randint(1, 100)

print(Name,'программа загадала число от 1 до 100')

while True:
    try:
        a = int(input('Введите число от 1 до 100: '))
        n += 1
    
        if a < random_number:
            print('Твое число меньше, попытайся еще')
        elif a > random_number:
            print('Твое число больше, попытайся еще')
        else:
            print('Ты угадал, это число', a,', ты использовал количество попыток -', n)

            Finish = str(input('Continue? (y/n): '))
            if  Finish == 'y':
                continue
            else:
                break
    except:
        print('Введите число')
      
