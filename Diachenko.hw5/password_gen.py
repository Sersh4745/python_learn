"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно (не влияет на оценку):
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""
# ОСНОВНОЕ ЗАДАНИЕ
from random import choice, randint
import string


def main():
    try:
        choice_pasword = int(input('Сгенерировать простой пароль - 1'
                                   'Сгенерировать средний пароль - 2'
                                   'Сгенерировать сложний пароль - 3:'))
    except ValueError:
        print('Введите число от 1 до 3')
        return main()
    length = 8  # для 1 и 2 задния
    length_2 = randint(8, 16)  # для 3

    small = string.ascii_lowercase
    big = string.ascii_uppercase
    spec = string.punctuation
    digits = string.digits
    all_symbols = spec+digits+big+small
    average = small+big+digits
    pas = ''
    if choice_pasword > 4:
        print('Введите число от 1 до 3')
        return main()
    if choice_pasword == 1:
        pas = pas + choice(small)
        while len(pas) < length:
            pas += choice(small)
    if choice_pasword == 2:
        pas = pas + choice(average)
        while len(pas) < length:
            pas += choice(average)
    if choice_pasword == 3:
        pas += choice(digits)
        pas += choice(small)
        pas += choice(big)
        pas += choice(spec)
        while len(pas) < length_2:
            pas += choice(all_symbols)
    print(pas)


main()

# ДОПОЛНИТЕЛЬНОЕ


def main1():
    words_for_password = input('Введите символы для будущего пароля: ')
    words = words_for_password.replace(' ', '')
    length_3 = int(input('Введите кол символов для пароля - "Больше 8" :'))
    pas = ''
    if len(words) < 8 or length_3 < 8:
        print('Пароль не надежный.\nВведите больше 8 символов')
        return main1()
    else:
        pas = pas + choice(words)
        while len(pas) < length_3:
            pas += choice(words)
    print(pas)


main1()
