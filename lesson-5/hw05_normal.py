<<<<<<< Updated upstream
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import hw05_easy

def gotodir():
    name_dir = input('введите путь, куда надо перейти: ')
    if os.path.exists(name_dir):
        os.chdir(name_dir)
        print('перешел в папку: {}'.format(name_dir))
    else:
        print('Невозможно перейти в указанную папку. Папка не существует.')

def deletedir():
    name_dir = input('введите имя папки, которую надо удалить: ')
    if os.path.exists(name_dir):
        os.rmdir(name_dir)
        print('папка {} удалена.'.format(name_dir))
    else:
        print('Невозможно удалить указанную папку. Папка не существует.')

print('1. Перейти в папку')
print('2. Просмотреть содержимое текущей папки')
print('3. Удалить папку')
print('4. Создать папку')
try:
    response = int(input('введите номер меню: '))
except ValueError:
    print('Введите число')
    sys.exit()

if response == 1:
    gotodir()
elif response == 2:
    hw05_easy.lsdir()
elif response == 3:
    deletedir()
elif response == 4:
    hw05_easy.createdir(1)
else:
    print('неопознаная команда')

=======
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import hw05_easy

def gotodir():
    name_dir = input('введите путь, куда надо перейти: ')
    if os.path.exists(name_dir):
        os.chdir(name_dir)
        print('перешел в папку: {}'.format(name_dir))
    else:
        print('Невозможно перейти в указанную папку. Папка не существует.')

def deletedir():
    name_dir = input('введите имя папки, которую надо удалить: ')
    if os.path.exists(name_dir):
        os.rmdir(name_dir)
        print('папка {} удалена.'.format(name_dir))
    else:
        print('Невозможно удалить указанную папку. Папка не существует.')

print('1. Перейти в папку')
print('2. Просмотреть содержимое текущей папки')
print('3. Удалить папку')
print('4. Создать папку')
try:
    response = int(input('введите номер меню: '))
except ValueError:
    print('Введите число')
    sys.exit()

if response == 1:
    gotodir()
elif response == 2:
    hw05_easy.lsdir()
elif response == 3:
    deletedir()
elif response == 4:
    hw05_easy.createdir(1)
else:
    print('неопознаная команда')

>>>>>>> Stashed changes
