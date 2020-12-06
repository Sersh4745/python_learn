"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, который не меньше размеров его ноги.

    Напишите программу, которая принимает список доступных размеров коньков и
    список размеров ног желающих.

    И выводит наибольшее количество людей,
    которые смогут покататься одновременно.


    Например:
    [in]
    [39, 38, 41, 37]
    [40, 39, 41]
39 38 41 37 40
40 39 41
    [out]
    2
"""
# Первый вариант
availuble = sorted(list(map(int, input('Введите доступные размеры:').split())))
desired = sorted(list(map(int, input('Введите размер ног желающих:').split())))
for i in availuble:
    count = 0
    for x in desired:
        if i >= x:
            count += 1
print(count)

# второй вариант
availuble = sorted(list(map(int, input('Введите доступные размеры:').split())))
desired = sorted(list(map(int, input('Введите размер ног желающих:').split())))
count = 0
while True:
    try:
        availuble = list(filter(lambda x: x >= min(desired), availuble))
        availuble.pop(0)
        desired.pop(0)
        count += 1
    except IndexError:
        break
print(count)
