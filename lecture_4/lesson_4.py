# def calc(a, b=1):
#     return a*b
#
#
# print(calc(5))
import datetime
# def person(age, f_name, l_name):
#     return f"Hello, my name is {f_name} {l_name}. I am {age} years old."
#
#
# print(person(f_name="Anna", age=20, l_name="Smith"))

# def pattern(length, char2, char1='*', ):
#     return (char1 + char2) * length + char1
#
#
# print(pattern(8, '-'))

# mult = lambda x, y: x*y
# print(mult(5, 6))

#отфильтровать список и получить из него только четные значения:

# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# l1 = [20, 15, 8, 7, 6]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, l))
#
# print(type(*filtered)) #вернется как filter object

# power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
# print(power)

# from functools import reduce
# result = reduce(lambda x, y: x - y, l1)
# print(result)


# def my_decorator(func):
#     def wrapper(arg):
#         print("I am wrapper")
#         func(arg)
#         print("Wrapped")
#     return wrapper
#
#
# @my_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")
#
#
# say_hello("Nick")

# def sugar(func):
#     def wrapper():
#         print("sugar")
#         func()
#     return wrapper
#
# def milk(func):
#     def wrapper():
#         print("hot milk")
#         func()
#     return wrapper
#
# @sugar
# @milk
# def coffee():
#     print('Coffee')
#
# coffee()

import datetime
import math

# bdate = 1980
# current_date = datetime.date.today()
# age = current_date.year - bdate
# сurrent_month = current_date.month
# print(age)
# print(сurrent_month)

# print(math.pow(3, 4))

# lst = [1, 2, 3]
# lst.reverse()
# print(lst)
# print(list(reversed(lst)))

# from module import hello, summa
# print(hello("Hanna"))
# print(summa(1, 2))

# print(milk.__name__)

