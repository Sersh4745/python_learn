"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).

    Перед записью в файл привести номер к формату +380501234567.
"""
import re


data = None
with open('python_basic/hw6/files/phone_book.txt') as f:
    data = f.readlines()

with open('Diachenko.hw6/edited_phone_book.txt', 'w') as file:
    cursor = data
    for i in cursor:
        i = re.sub(r'\W', '', i).lower()
        if i[0] == 'м' or re.sub(r'\d', '', i)[-1] == 'а':
            file.write('380' + re.sub(r'\D', '', i)[-9:] + '\n')
