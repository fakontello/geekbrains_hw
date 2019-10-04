# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

from math import sqrt

def F(i):
    return ((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))

def fibonacci(n, m):
    i = 0
    cur = F(i)
    while cur <= m:
        if n <= cur:
            print(cur)
        i += 1
        cur = F(i)


print(fibonacci(1, 10))
    

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list) - 1, i, -1):
            if origin_list[j] < origin_list[j - 1]:
                origin_list[j], origin_list[j - 1] = origin_list[j - 1], origin_list[j]

    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def own_filter(a): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (a in letters): 
        return True
    else: 
        return False

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

from math import sqrt

print('Проверим, являются ли точки A, B, C и D вершинами параллелограмма')

x1 = int(input('Введите первую координату точки A: \n'))
y1 = int(input('Введите вторую координату точки A: \n'))
x2 = int(input('Введите первую координату точки B: \n'))
y2 = int(input('Введите вторую координату точки B: \n'))
x3 = int(input('Введите первую координату точки C: \n'))
y3 = int(input('Введите вторую координату точки C: \n'))
x4 = int(input('Введите первую координату точки D: \n'))
y4 = int(input('Введите вторую координату точки D: \n'))

#   A1(x1, y1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4)
#   A(1,3), B(4,7), C(2,8), D(-1,4)

AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
DC = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
AD = sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)


if AB == DC and BC == AD:
    print('Да, это параллелограмм!')
else:
    print('Нет, точки не являются вершинами')
