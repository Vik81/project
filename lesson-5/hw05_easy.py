# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория существует')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for i in os.listdir():
    if os.path.isdir(i):
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

name_new_file = os.path.split(sys.argv[0])
name_new_file = '{}/new_{}'.format(name_new_file[0], name_new_file[1])
shutil.copy(sys.argv[0], name_new_file)
# print(name_new_file)