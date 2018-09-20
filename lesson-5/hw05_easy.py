# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

def createdir(n): # кол-во папок
    try:
        n = int(n)
    except:
        print('введите целое число')
    for i in range(1, n + 1):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.mkdir(dir_path)
            print('Папка {} создана'.format(dir_path))
        except FileExistsError:
            print('Такая директория существует')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def lsdir():
    for i in os.listdir():
        # if os.path.isdir(i):   # по условию задачи должны бать только папки, но по normal - содержимое папки
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def cpfile():
    name_new_file = os.path.split(sys.argv[0])
    name_new_file = '{}/new_{}'.format(name_new_file[0], name_new_file[1])
    shutil.copy(sys.argv[0], name_new_file)