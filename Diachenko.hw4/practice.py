string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '

string1 = ''.join(string.split(','))
print('1 ', string1)

# 2. Вывести индекс самой последней буквы 's' в строке.

string2 = string.rindex('s')
print('2. Индекс последней буквы s:', string2)

# 3. Вывести количество букв 'i' в строке (регистр не имеет значения).

string3 = string.lower()  # Переводим все в один регистр и затем считаем
print('3. Количество букв i:', string3.count('i'))

# 4. Вывести срез строки.
str4 = string1.find('simply')
str41 = (string1.rfind('of')) - 1  # выводим of и отнимаем 1 поскольку of невкл

print('4. Выводим срез:', string1[str4:str41])

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной.
string5 = int((string1.find('.')-1) / 2)  # узнаем половину символов строки
str5 = (string1[:string5])  # Левая половина предложения
str6 = (string1[string5:])  # Правая половина
print('5 ', str5*3 + str6)
