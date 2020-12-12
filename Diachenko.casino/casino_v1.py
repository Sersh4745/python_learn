"""
    Casino

    ** для высшего балла хранить статистику игроков в файле
        и при каждом запуске casino запрашивать имя игрока.

    При запуске программы:
        - игроку необходимо ввести имя
        - попадаем в Главное меню
        * возможно у игрока должно быть изначально какое-то количество очков

    Главное меню:
    1. Magic
    2. Blackjack (21)
    3. Посмотреть статистику
    4. Сбросить игровой прогресс

    При выборе пункта 1.
        - выводятся правила игры
        - запускается игра magic (hw3/magic.py)
        - в игре ограниченное количество попыток
        * придумать правила начисления очков при угадывании с 1, 2 .. N попыток
        * придумать правила потери очков при проигрыше

    При выборе пункта 2.
        - выводятся правила игры
        - игрок делает ставку (не больше, чем у него имеется очков)
        - запускается игра blackjack (21)

    При выборе пункта 3.
        - выводится подробная статистика игрока:
            Имя игрока: Max
            Количество очков: 190

            Magic
            Всего игр сыграно: 20
            Выиграно: 5
            Коэффициент выигрышей: 0.25
            Рекордное количество попыток: 2

            Blackjack
            Всего игр сыграно: 0
            Выиграно: 0
            Коэффициент выигрышей: -

    При выборе пункта 4.
        - удаляются данные игрока
        - запрашивается имя нового игрока
        - попадаем в Главное меню


    Реализаци blackjack (правила https://en.wikipedia.org/wiki/Blackjack):
        - формируется колода карт
            от двойки до десятки — от 2 до 10 соответственно,
            у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1),
            у т.н. картинок (король, дама, валет) — 10.

            в итоге колода - [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        - колода перетосовывается с помощью random.shuffle()
        - игроку предлагается на выбор:
            1. взять ещё карту
                - из колоды исключается одна карта и дается игроку
            2. остановиться

        - если у игрока в сумме выходит 21 - победа (игроку возвращается удвоенная ставка)
        - если у игрока в сумме выходит больше 21 (перебор) - проигрыш (ставка снимается в пользу казино)
        - если игрок остановился на сумме меньше 21 - ставка возвращается игроку

        * описынные выше правила можно дополнить по желанию
"""

import random

name = input('Введите свое имя: ').capitalize()
point = 100  # заработанные балы. Изначально 100
pusk_plus = 0  # счетчик выиграшей
payoff_ratio = 0  # коэф выиграшей
random_number = random.randint(1, 100)
counter = 0  # счетчик попыток
counter_pusk = 0  # счетчик запусков общий
record_counter = 0  # рекордное число попыток
count_play = 0
play_win = 0
payoff_rat = 0


def main():
    print('''Главное меню:
    1. Magic
    2. Blackjack (21)
    3. Посмотреть статистику
    4. Сбросить игровой прогресс''')
    try:
        choice_ = int(input('\nВведите свой выбор: '))
    except ValueError:
        print('Введите число от 1 до 4')
        return main()
    if choice_ == 1:
        magic_()
        # login()
    if choice_ == 2:
        Blackjack()
        # login()
    if choice_ == 3:
        info_funck()
    if choice_ == 4:
        func_4()


def magic_():
    global point
    global pusk_plus
    global payoff_ratio
    global random_number
    global counter
    global counter_pusk
    global record_counter

    print('\nПривет. Это программа "Магическое число"')
    while True:
        try:
            number = int(input('Введите число от 1 до 100: \n'))
            counter += 1
        except ValueError:
            continue

        if counter >= 25:  # дано 25 попыток угадать число
            print('Вы проиграли: ')
            point -= 5  # отнимает бал при проиграше
            counter_pusk += 1
            payoff_ratio = pusk_plus/counter_pusk

            if input('\nContinue? (y/n) ') != 'y':
                return main()
            random_number = random.randint(1, 100)
            counter = 0
        if number > random_number:
            print('Твое число больше, попытайся еще')
        elif number < random_number:
            print('Твое число меньше, попытайся еще')
        else:
            print('\nТы угадал, это число ', number)
            if record_counter == 0:
                print('Супер, Это рекорд! Кол попыток: ', counter)
                record_counter = counter
            elif counter < record_counter:
                print('Супер, Это рекорд! Кол попыток: ', counter)
                record_counter = counter
            else:
                print('Кол пыпыток: ', counter)
            if counter <= 5:
                point += 25
            if counter > 5:
                point += 20
            pusk_plus += 1
            counter_pusk += 1
            payoff_ratio = pusk_plus/counter_pusk

            if input('\nContinue? (y/n) ') != 'y':
                return main()
            random_number = random.randint(1, 100)
            counter = 0


def Blackjack():
    global point
    koloda = [
                6, 7, 8, 9, 10, 2, 3,
                4, 10, 10, 10, 10, 11, 5
    ] * 4 * random.randint(1, 8)
    # от 1 до 8 колод
    global count_play
    global play_win
    global payoff_rat
    random.shuffle(koloda)
    print('''Игра Blackjack
    Правила:
    Участник берет карту до тех пор - пока не достигнет в сумме 21
    Если сумма карт выше 21 - то Вы проиграли''')
    count = 0
    try:
        rate = int(input('\nСделайте ставку: '))  # ставка
        count_play += 1
        if point < rate:  # проверка ставки с балами
            return Blackjack()
    except ValueError:
        return Blackjack()

    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            current = koloda.pop()
            print('Вам попалась карта достоинством', current)
            count += current
            if count > 21:
                point -= rate  # отнимаем ставку в случе проиграша
                print('Увы перебор')
                return main()
            elif count == 21:
                point *= 2
                point += rate
                play_win += 1
                print('Поздравляю, вы набрали 21!')
                return main()
            else:
                print('У вас', count, 'очков.')
            payoff_rat = play_win/count_play

        elif choice != 'y':
            print('У вас', count, 'очков и вы закончили игру.')
            return main()


def task_1():
    with open('Diachenko.casino/magic.txt', 'w') as f:
        print('\nMagic', file=f)
        print('Всего игр сыграно: ', counter_pusk, file=f)
        print('Выиграно: ', pusk_plus, file=f)
        print('Коэфициент выграшей: ', payoff_ratio, file=f)
        print('Рекордное количество попыток: ', record_counter, file=f)


def task_2():
    with open('Diachenko.casino/black.txt', 'w') as f:
        print('\nBlackjack', file=f)
        print('Всего игр сыграно: ', count_play, file=f)
        print('Выиграно: ', play_win, file=f)
        print('Коэфициент выграшей: ', payoff_rat, file=f)


def login():
    task_1()
    task_2()
    with open('Diachenko.casino/black.txt', 'r') as f:
        text_black = f.read()

    with open('Diachenko.casino/magic.txt', 'r') as f:
        text_magic = f.read()
        with open('Diachenko.casino/casino.txt', 'w') as f:
            print('\nИмя игрока:', name, file=f)
            print('Количество очков:', point, file=f)
            f.write(text_magic)
            f.write(text_black)


def info_funck():
    login()
    with open('Diachenko.casino/casino.txt') as f:
        print(f.read())
    if input('\nContinue? (y/n) ') == 'y':
        return main()


def func_4():
    global name
    global point
    global pusk_plus
    global payoff_ratio
    global counter
    global counter_pusk
    global record_counter
    global count_play
    global play_win
    global payoff_rat
    name = input('Введите свое имя: ').capitalize()
    open('Diachenko.casino/casino.txt', 'w').close()
    point = 100
    pusk_plus = 0
    payoff_ratio = 0
    counter = 0
    counter_pusk = 0
    record_counter = 0
    count_play = 0
    play_win = 0
    payoff_rat = 0
    return main()


main()
