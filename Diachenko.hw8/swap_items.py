"""
    Напишите функцию, которая принимает словарь,
    меняет местами ключи и значения и возвращает его.

    Покройте функцию несколькими тестами.

    Пример:
    a = {'key': 'value', 'd': 1234}
    b = swap_items(a)
    print(b)
    {'value': 'key', 1234: 'd'}

    * пропускайте пары, в которых значение не может быть ключем

    ** ключем словаря может быть только не изменяемый объект,
        а точнее тот, который можно захешировать функцией hash()

"""


def input_funck(d):
    y = {}
    for k, v in d.items():
        try:
            y[v] = k
        except TypeError:
            continue
    return y


t1 = {'1': 'asd', '2': 'asdd'}
assert input_funck(t1) == {'asd': '1', 'asdd': '2'}

t2 = {'key': 'value', 'd': 1234}
assert input_funck(t2) == {'value': 'key', 1234: 'd'}

assert input_funck({'a': [1, 2, 3], 'b': 123}) == {123: 'b'}