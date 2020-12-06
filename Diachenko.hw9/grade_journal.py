"""
    Пользователь вводит количество студентов n.
    После чего вводит n строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""


def main():
    in_d = input_dictionary()
    list_2 = sorted(in_d.items(), key=lambda data: data[1], reverse=True)
    for i, item in enumerate(list_2):
        print(i + 1, item[0])


def input_dictionary():
    try:
        n = int(input('Введите количество студентов: '))
    except ValueError:
        return input_dictionary()
    str_list = dict([input('Ввод фамилию и балл: ').split() for _ in range(n)])
    return str_list


main()
