string = input('Ввод: ')
lows = 0
ups = 0

for i in string:
    if i.islower():
        lows += 1
    elif i.upper():
        ups +=1
print('Нижний',lows)
print('Верхний',ups)

if lows > ups:
    print('1.',string.lower())
elif lows < ups:
    print('1.',string.upper())
else:
    print('1.',string.swapcase())

#2. Если в строке каждое слово начинается с заглавной буквы, тогда добавить в начало строки 'done. '.


if string.istitle():
    print('2. done ' + string)
else :
    print('2.',(string.replace(string, "draft ",5)) + string[5:])
     

   #3. Если длина строки больше 20, то обрезать лишние символы до 20. 


if len(string) > 20:
    print('3. Исходная строка:', string)
    print('Результат:', string[:20])

elif len(string) < 20:
    print('3. Исходная строка:', string)
    print('Результат:', (string + (20 - len(string))*'@'))
