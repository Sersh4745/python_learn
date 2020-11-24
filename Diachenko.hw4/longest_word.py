"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

x = input('Введите значение: ').split()
line_lenth = len(x)
print('Количество слов:', line_lenth)
count = 0
for i in x:
    if len(i) > count:
        count = len(i)
        words = i
        print('Самое длинное слово:', words, ';')
        print('Его длина составлет:', count, '.')
