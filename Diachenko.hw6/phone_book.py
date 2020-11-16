"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).

    Перед записью в файл привести номер к формату +380501234567.
"""
from os import curdir
import re
from re import split

data = None
with open('C:/Users/Sersh/python_basic/python_basic/hw6/files/phone_book.txt') as f:
    data = f.read()

with open('Diachenko.hw6/edited_phone_book.txt','w') as file:
    #cursor = re.sub(r'\D','', phone_number)
    cursor = data.lower()
    #cursor = cursor.lstrip()
    cursor = cursor.replace(' ','') 
    cursor = cursor.replace('(','')
    cursor = cursor.replace(')','')
    cursor = cursor.replace('+','')
    cursor = cursor.replace('-','') 
    cursor = cursor.split()

    for i in cursor:
        if i[0] == 'м':
            file.write('380'+ re.sub(r'\D','',i)[-9:]+ '\n') #вывел все номера которые совпадают с условиями

        if re.sub(r'\d','',i)[-1] == 'а':
            file.write('380'+ re.sub(r'\D','',i)[-9:]+ '\n')


       




