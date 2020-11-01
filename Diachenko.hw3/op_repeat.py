x = input('Введите число: ')

while type(x) != int:
    try:
        x = int(x)
    except:
        print('Не число')
        x = input('Введите число: ')
        continue
        
    if x <= 9999 or x >= 100000 :
            print('Введите пятизначное число')
            x = input('Введите число: ')
    else:
            print(str(x // 10000) + '0' + str((x // 100) % 10) + '0' +  str(x % 10))
          

