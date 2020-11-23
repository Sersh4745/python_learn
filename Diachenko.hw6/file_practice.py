"""
    Выполните все пункты.

    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее кол
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое

with open('Diachenko.hw6/file_practice.txt', 'w') as file:
    print('Starting practice with files', file=file)

with open('Diachenko.hw6/file_practice.txt') as file:
    words = file.read()
    print('2.', words)
    print('2.', words[:5])

with open('Diachenko.hw6/file_practice.txt', 'r+') as file:
    words = file.read()
    count_i = 0
    count_e = 0
    for x in words:
        if x == 'i':
            count_i += 1
        if x == 'e':
            count_e += 1
    if count_i > count_e:
        words = words.replace('i', 'e')
    else:
        words = words.replace('e', 'i')
    file.write(words)

with open('Diachenko.hw6/file_practice.txt', 'r+') as file:
    words = file.read()
    file.write('*some pasted text*')
    cursor = file.tell()
    if cursor % 2 == 0:
        file.write('\nthe end')
    else:
        file.write('\nbye')

with open('Diachenko.hw6/file_practice.txt', 'r') as file:
    print(file.read())
