"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import random

class Card:
    def __init__(self):
        self._crd = [['  ','  ','  ', '  ', '  ','  ','  ','  ', '  '],['  ','  ','  ', '  ', '  ','  ','  ','  ', '  '],['  ','  ','  ', '  ', '  ','  ','  ','  ', '  ']]

    def create_card(self):    # создание карты игрока
        lst = random.sample(range(1, 91), 15)
        for i in range(3):
            for j in range(5):
                self._crd[i][j] = lst[0]
                lst.remove(lst[0])
            random.shuffle(self._crd[i])

    def find_barrel(self, barrel):  # ищем бочнок
        for i in range(3):
            for j in range(9):
                if barrel == self._crd[i][j]:
                    return True
        return False

    def del_barrel(self, barrel):
        for i in range(3):
            for j in range(9):
                if barrel == self._crd[i][j]:
                    self._crd[i][j] = '--'

    def show_card(self):  # вывести на экран
        print('--------------------------')
        for i in range(3):
            for j in range(9):
                print('{} '.format(self._crd[i][j]), end='')
            print()
        print('--------------------------')

    def valid(self): # проверка на выйгрыш
        for i in range(3):
            for j in range(9):
                if str(self._crd[i][j]).isdigit():
                    return True
        return False


class CardComp(Card):
    def __init__(self):
        super().__init__()

    def show_card(self):  # вывести на экран
        print('-- Карточка компьютера ---')
        for i in range(3):
            for j in range(9):
                print('{} '.format(self._crd[i][j]), end='')
            print()
        print('--------------------------')

class CardPlayer(Card):
    def __init__(self):
        super().__init__()

    def show_card(self):  # вывести на экран
        print('------ Ваша карточка -----')
        for i in range(3):
            for j in range(9):
                print('{} '.format(self._crd[i][j]), end='')
            print()
        print('--------------------------')

class Bag:
    def __init__(self):
        self._bag = [i for i in range(1,91)]
        self.barrel = ''

    def pull(self):   # вытянуть бочнок
        self.barrel = random.choice(self._bag)
        self._bag.remove(self.barrel)
        return self.barrel

    def remained(self):  # кол-во оставшихся бочонков
        return len(self._bag)


comp_card = CardComp()
comp_card.create_card()
player_card = CardPlayer()
player_card.create_card()
bag = Bag()

while True:
     print('Новый бочонок: {} (осталось {})'.format(bag.pull(), bag.remained()))
     comp_card.show_card()
     player_card.show_card()
     if input('Зачеркнуть цифру? (y/n)') == 'y':
         if player_card.find_barrel(bag.barrel) or comp_card.find_barrel(bag.barrel):
             player_card.del_barrel(bag.barrel)
             comp_card.del_barrel(bag.barrel)
         else:
             print('Вы проиграли')
             break
     else:
         if player_card.find_barrel(bag.barrel) or comp_card.find_barrel(bag.barrel):
             print('Вы проиграли')
             break
     if not player_card.valid():
         player_card.show_card()
         print('Вы выиграли')
         break
     elif not comp_card.valid():
         comp_card.show_card()
         print('Выиграл компьютер')
         break