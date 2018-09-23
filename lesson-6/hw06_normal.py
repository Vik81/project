# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, armor=0.7, health=100, damage=50):
        self._name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, damage, armor):
        return self.damage // self.armor

    def attack(self, who_attack, who_defend):
        damage = self.calculate_damage(who_attack.damage, who_defend.armor)
        who_defend.health -= damage
        # print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, damage,
        #                                                                 who_defend.health))

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_game(self, player, enemy):
        last_attacker = self.player
        while self.player.health > 0 and self.enemy.health > 0:
            if last_attacker == self.player:
                self.attack(enemy, player)
                last_attacker = self.enemy
            else:
                self.attack(player, enemy)
                last_attacker = self.player

        if self.player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')

class Player(Person):
    pass

class Enemy(Person):
    pass