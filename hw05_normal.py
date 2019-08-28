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

# Содержимое файла easy.py

import os
import shutil

if __name__ == '__main__':
    print('Easy')


def create_folders(name):
    try:
        os.makedirs(name)
        print(f'Вы успешно создали папку {name}')
    except FileExistsError:
        print(f'{name} - уже существует')


if __name__ == '__main__':
    create_folders()


def remove_folders(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print(f'{name} - папки не существует')


if __name__ == '__main__':
    remove_folders()


def list_dir():
    a = os.listdir()
    print('Список папок:')
    for index, element in enumerate(a, start=1):
        if os.path.isdir(element):
            print(f'{index}. {element}')


if __name__ == '__main__':
    list_dir()


def current_file_copy():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - успешно создан'
    else:
        return 'Файл уже был скопирован'


if __name__ == '__main__':
    current_file_copy()


def change_dir(path):
    try:
        os.chdir(path)
        print(f'Теперь вы в папке {path}')
    except FileNotFoundError:
        print(f'{path} - папки не существует')


if __name__ == '__main__':
    change_dir()
# Решение задачи:

import os
import easy as easy


def start():
    answer = ''
    while answer != '5':
        print('-'*20)
        print('Текущая директория: ' + os.getcwd())
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer == '5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода(для возврата напишите .. : ')
            easy.change_dir(path_name)
        elif answer == '2':
            easy.list_dir()
        elif answer == '3':
            name = input('Введите имя удаляемой папки: ')
            easy.remove_folders(name)
        elif answer == '4':
            name = input('Введите имя новой папки: ')
            easy.create_folders(name)


if __name__ == '__main__':
    start()