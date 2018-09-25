# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'машина поехала')

    def stop(self):
        print(self.name, 'машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(self.name, 'повернула налево')
        elif direction == 'right':
            print(self.name, 'повернула направо')


class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'машина поехала')

    def stop(self):
        print(self.name, 'машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(self.name, 'повернула налево')
        elif direction == 'right':
            print(self.name, 'повернула направо')


class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'машина поехала')

    def stop(self):
        print(self.name, 'машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(self.name, 'повернула налево')
        elif direction == 'right':
            print(self.name, 'повернула направо')


# class PoliceCar:
#     def __init__(self, speed, color, name, is_police=True):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print(self.name, 'машина поехала')
#
#     def stop(self):
#         print(self.name, 'машина остановилась')
#
#     def turn(self, direction):
#         if direction == 'left':
#             print(self.name, 'повернула налево')
#         elif direction == 'right':
#             print(self.name, 'повернула направо')


vw = TownCar(90, 'red', 'Golf')

vw.turn('left')

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'машина поехала')

    def stop(self):
        print(self.name, 'машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(self.name, 'повернула налево')
        elif direction == 'right':
            print(self.name, 'повернула направо')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

police = PoliceCar(110, 'black', 'BMW')
print(police.is_police)