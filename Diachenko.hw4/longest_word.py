x = input('Введите значение: ')

#Узнаем количество слов в строке

x = x.split()
line_lenth = len(x)
print('Количество слов:',line_lenth)

#Узнаем самое длинное слово и его длину

count = 0
for i in x :
    if len(i) > count:
        count = len(i)
        words = i
print('Самое длинное слово:', words,';')
print('Его длина составлет:',len(words),'.')