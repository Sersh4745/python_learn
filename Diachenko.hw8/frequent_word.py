"""
    Напишите функцию, которая приинимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""
import re


def ret_words(text):
    # использовал регулярку вместо split
    text = re.findall(r'[a-zA-Z]+', text)
    words = {}
    for w in text:
        words[w] = words.get(w, 0) + 1
    max_words = max(words.values())

    for key, value in words.items():
        if value == max_words:
            print(key)
            return key


t_2 = 'blue, red, blue, yellow, red, blue, green, yellow, black'
assert ret_words(t_2) == 'blue'

t_3 = 'a, abc, cbd, zzzzzz, a, abc, def, asasa, abc, aaaaaa'
assert ret_words(t_3) == 'abc'
