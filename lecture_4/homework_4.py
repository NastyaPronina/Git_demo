import time
from functools import reduce
from math import sqrt
# 4.1 Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

# def square(a):
#     return 4 * a, a ** 2, round(sqrt(a ** 2 * 2), 2)
#
#
# print(square(4))

# 4.2 Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")
#
#
# func(name='Anna', l_name='Pavlova', age=35, position='developer')

# 4.3 Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# положительные числа

# lst = [20, -3, 15, 2, -1, -21]
# filtered = list(filter(lambda x: x > 0, lst))
#
# print(filtered)

# 4.4 Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# lst = [20, -3, 15, 2, -1, -21]
# multiplication = reduce(lambda x, y: x*y, lst)
#
# print(multiplication)

# 4.5 Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

# def time_execution(func):
#     def wrapper():
#         start = time.perf_counter()
#         func()
#         end = time.perf_counter()
#         result = end - start
#         print(f'{func.__name__} execution time is: {result}')
#     return wrapper
#
# @time_execution
# def initial():
#     print("Initial function")
#
# initial()

# Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.

# import my_calc
# print(my_calc.difference(10, 30))
# print(my_calc.multiply(5, 7))
# print(my_calc.devide(5, 5))

