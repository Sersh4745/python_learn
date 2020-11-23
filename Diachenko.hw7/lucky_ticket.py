"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(lucky):
    lucky = str(lucky)
    length = (len(lucky) + 1)//2
    part_1 = lucky[0:length]
    part_2 = lucky[length:]
    part_11 = []
    part_12 = []

    for i in part_1:
        part_11.append(int(i))
    for w in part_2:
        part_12.append(int(w))
    if sum(part_11) == sum(part_12):
        return True
    else:
        return False


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
