import json
import random


STATISTIC_TEMPLATE = """
Имя игрока: {name}
Количество очков: {points}

Magic:
    Всего игр сыграно: {magic_games}
    Выиграно: {magic_wins}
    Коэфициент выграшей: {mg_kof}
    Рекордное количество попыток: {mg_rec}

BlackJack:
    Всего игр сыграно: {bj_games}
    Выиграно: {bj_wins}
    Коэфициент выграшей: {bj_kof}
"""


class Casino:
    player_name = None
    player_data = {
        'points': 100,
        'magic': {
            'games': 0,
            'wins': 0,
            'record': None
        },
        'blackjack': {
            'games': 0,
            'wins': 0
        }
    }

    def __init__(self):
        """
            Создаем файл при инициализации, если его нет.
            Таким образом файл всегда будет существовать.

        """
        try:
            with open('casino.json', 'x') as f:
                data = json.dumps({})
                f.write(data)
        except FileExistsError:
            """
                TODO: Здесь можно добавить доп проверку, если вдруг файл пустой
                и не содержит {} (пустого словаря), тогда его пересоздать.

                (не обязательно)
            """

    def launch(self):
        """ Запуск игры. Авторизация и переход в главное меню. """
        self.login()
        self.main_menu()

    def login(self):
        """
            Авторизация и запись информации об игроке.

            Пользователь вводит имя, в файле casino.json по ключу его имени
            получаем его данные.
            Если данных по такому имени не существует, то
            создаем их.

            После получения/создания записываем в атрибут player_data
        """
        name = input('Добро пожаловать! Представьтесь: ').capitalize()
        self.player_name = name  # имя сразу записываем в атрибут player_name

        with open('casino.json', 'r') as f:
            data = json.load(f)  # читаем json и превращаем его в словарь
            # получаем данные игрока из файла и записываем в self.player_data,
            # а если их нет, то оставляем дефолтные, которые уже записаны
            self.player_data = data.get(name, self.player_data)

    def main_menu(self):
        """ Отображение главного меню, запуск выбраных пунктов. """
        choice = input(
            '\nГлавное меню (введите нужный пункт):\n'
            '1. Magic\n'
            '2. Blackjack (21)\n'
            '3. Посмотреть статистику\n'
            '4. Сбросить игровой прогресс\n'
        )
        if choice == '1':
            self.magic()
        elif choice == '2':
            self.blackjack()
        elif choice == '3':
            self.statistic()
        elif choice == '4':
            self.reset()
        elif choice == '5':
            self.__del__()
        else:
            return self.main_menu()

    def magic(self):
        """
            TODO: Здесь будет игра Magic.

            После каждой игры обновляем информацию в self.player_data,
            а именно количество игр "games", количество побед "wins" и
            рекорд "record", если он побит.

            Сравнивать рекорд и обновлять инфу по ключам.
            рекорд - self.player_data['magic']['record']
            количество игр - self.player_data['magic']['games']
            и т.д.
        """
        random_number = random.randint(1, 100)
        counter = 0
        print('\nПривет. Это программа "Магическое число"')
        while True:
            try:
                number = int(input('Введите число от 1 до 100: \n'))
                counter += 1
            except ValueError:
                continue

            if counter >= 25:  # дано 25 попыток угадать число
                print('Вы проиграли: ')
                self.player_data['points'] -= 5
                self.player_data['magic']['games'] += 1

                if input('\nContinue? (y/n) ') != 'y':
                    return self.main_menu()
                random_number = random.randint(1, 100)
                counter = 0
            if number > random_number:
                print('Твое число больше, попытайся еще')
            elif number < random_number:
                print('Твое число меньше, попытайся еще')
            else:
                print('\nТы угадал, это число ', number)
                if self.player_data['magic']['record'] is None:
                    print('Супер, Это рекорд! Кол попыток: ', counter)
                    self.player_data['magic']['record'] = counter
                elif counter < self.player_data['magic']['record']:
                    print('Супер, Это рекорд! Кол попыток: ', counter)
                    self.player_data['magic']['record'] = counter
                else:
                    print('Кол пыпыток: ', counter)
                if counter <= 5:
                    self.player_data['points'] += 25
                if counter > 5:
                    self.player_data['points'] += 20
                self.player_data['magic']['wins'] += 1
                self.player_data['magic']['games'] += 1

                if input('\nContinue? (y/n) ') != 'y':
                    return self.main_menu()
                random_number = random.randint(1, 100)
                counter = 0

    def blackjack(self):
        """
            TODO: Здесь будет игра BlackJack.

            После каждой игры обновляем информацию в self.player_data,
            а именно количество игр "games" и количество побед "wins".

            Обновлять инфу по ключам, аналогично с Magic.
        """

        koloda = [
                    6, 7, 8, 9, 10, 2, 3,
                    4, 10, 10, 10, 10, 11, 5
        ] * 4 * random.randint(1, 8)
        # от 1 до 8 колод
        count = 0
        random.shuffle(koloda)
        print('''Игра Blackjack
        Правила:
        Участник берет карту до тех пор - пока не достигнет в сумме 21
        Если сумма карт выше 21 - то Вы проиграли''')

        try:
            rate = int(input('\nСделайте ставку: '))  # ставка
            self.player_data['blackjack']['games'] += 1
            if self.player_data['points'] < rate:  # проверка ставки с балами
                return self.blackjack()
        except ValueError:
            return self.blackjack()

        while True:
            choice = input('Будете брать карту? y/n\n')
            if choice == 'y':
                current = koloda.pop()
                print('Вам попалась карта достоинством', current)
                count += current
                if count > 21:
                    self.player_data['points'] -= rate
                    print('Увы перебор')
                    return self.main_menu()
                elif count == 21:
                    self.player_data['points'] *= 2
                    self.player_data['points'] += rate
                    self.player_data['blackjack']['wins'] += 1
                    print('Поздравляю, вы набрали 21!')
                    return self.main_menu()
                else:
                    print('У вас', count, 'очков.')

            elif choice != 'y':
                print('У вас', count, 'очков и вы закончили игру.')
                return self.main_menu()

    def statistic(self):
        """
            TODO: Здесь будет формироваться и выводится статистика.

            Просчитываются коэфициэнты,
            составляется нужное сообщение с помощью форматирования строк.
        """
        s = self.player_name
        p = self.player_data['points']
        g = self.player_data['magic']['games']
        w = self.player_data['magic']['wins']
        r = self.player_data['magic']['record']
        bw = self.player_data['blackjack']['wins']
        br = self.player_data['blackjack']['games']
        mg_k = w/g if g != 0 else 0.0
        r = r if r is not None else 0
        bj_k = bw/br if br != 0 else 0.0

        statistic = STATISTIC_TEMPLATE.format(
            name=s, points=p, magic_games=g, magic_wins=w, mg_rec=r,
            mg_kof=mg_k, bj_games=br, bj_wins=bw, bj_kof=bj_k
        )
        print(statistic)
        choice_ = input('\nВывести главное меню? (y/n) ')

        if choice_ == 'y':
            return self.main_menu()
        else:
            print('\nДо встречи !')

    def reset(self):
        """
            TODO: Здесь будет сбрасываться прогресс игрока.

            Можно просто удалять его данные и заново запускать self.launch().
            Либо просто обнулять все показатели по имени игрока.

            Либо сделать выбор: обнулить статистику или удалить игрока.
        """
        print('\nУдалить прогрес игрока', self.player_name, '?')
        if input('y or n: ') == 'y':
            del self.player_data
            self.__del__()
        return self.launch()

    def __del__(self):
        """ При удалении экземпляра обновляем информацию в файле """
        with open('casino.json', 'r+') as f:
            data = json.load(f)
        data[self.player_name] = self.player_data
        json_data = json.dumps(data, indent=4)
        with open('casino.json', 'w') as f:
            f.write(json_data)


def main():
    game = Casino()
    game.launch()


if __name__ == '__main__':
    main()
