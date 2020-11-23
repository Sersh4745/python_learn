"""
    Реализовать функции, которые принимают 2 списка чисел и:

    1 функция
    Возвращает список чисел (в порядке возрастания),
    которые содержатся в первом и втором списке одновременно.

    2 функция
    Возвращает список чисел (в порядке убывания),
    которые не содержатся в первом и втором списке одновременно.

    3 функция
    Возвращает количество уникальных чисел,
    которые содержатся во втором списке, но не содержатся в первом.
"""


list_1 = input('Введите сисок №1: ').split()
list_2 = input('Введите сисок №2: ').split()
print(list_1)


def funck_1():
    list_general = list_1 + list_2
    print(sorted(list_general))


funck_1()


def funck_2():
    list_3 = set(list_1)
    list_4 = set(list_2)
    list_diff = sorted((list_3 ^ list_4), reverse=True)
    print(list_diff)


funck_2()


def funck_3():
    list_5 = set(list_1)
    list_6 = set(list_2)
    list_diff_2 = sorted(list_6-list_5)
    print(list_diff_2)


funck_3()
