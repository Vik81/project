# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def name(first_name, age, city):
    s = '{}, {} год(а), проживает в гооде {}'.format(first_name, age, city)
    return s


print(name('Василий', 21, 'Москва'))


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def maximus(a, b, c):
    return max(a, b, c)


print(maximus(3, 10, 5))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def strlen(*args):
    s = max(*args, key=len)
    return s


s = strlen('sdfg', 'sdfgdsfgsd', 'dfg')
print(s)
