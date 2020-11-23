"""
    Пользователь вводит количество групп n.
    Далее вводится n строк, каждая строка начинается с названия группы,
    а затем через пробел идут элементы группы.

    1. Обработать строки и вывести на экран словарь, в котором
    ключи - это группы, а значения - списки элементов групп.
    2. Создать и вывести второй словарь, в котором
    ключи - элементы групп, а зачения - группы.

    Используйте функции!

    Например:
    [out] Введите кол-во групп:
    [in]  2

    [out] 1 группа:
    [in]  fruits apple banana mango kiwi lemon

    [out] 2 группа:
    [in]  citrus lime lemon orange

    [out] {
        'fruits': ['apple', 'banana', 'mango', 'kiwi', 'lemon'],
        'citrus': ['lime', 'lemon', 'orange']
    }
    [out] {
        'apple': ['fruits'],
        'lemon': ['citrus', 'fruits'],
        ...
    }
"""


def main():
    for i in input_dictionary():
        i = i.split()
        dict = {'key': i[0], 'val': ' '. join(i[1:])}
        dict_2 = {'key':  ' '. join(i[1:]), 'val': i[0]}
        print(dict)
        print(dict_2)


def input_dictionary():
    n = int(input('Вводим количество строк: '))
    str_list = []
    for i in range(n):
        line = input('Ввод (сначала имя группы, потом значения): ')
        str_list.append(line)
    return str_list


main()
