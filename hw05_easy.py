# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

if __name__ == '__main__':
    print('Задача №1 (easy)')

def create_folders():
    ''' Создание папок '''
    for i in range(10):
        path = f'dir_{i}'
        if not os.path.exists(path):
            os.mkdir(path)
            
if __name__ == '__main__':            
	create_folders()         
            

def remove_folders():
    ''' Удаление папок '''
    for i in range(10):
        path = f'dir_{i}'
        if os.path.exists(path):
            os.rmdir(path)
           
if __name__ == '__main__':         
	remove_folders()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir ():
    a = os.listdir()
    print('Список папок:')
    for index, element in enumerate(a, start=1):
        if os.path.isdir(element):
            print(f'{index}. {element}')


if __name__ == '__main__':
    list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - успешно создан'
    else:
        return 'Файл уже был скопирован'


if __name__ == '__main__':
    print(current_file_copy())
