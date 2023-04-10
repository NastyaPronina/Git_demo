#1 Дан список my_list. Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])

#2 Дан список list_1. Получите сумму всех чисел, распечатайте все строки, где есть буква 'a'.

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#
# list_2 = [x for x in list_1 if isinstance(x, int)]
# print(sum(list_2))
#
# list_3 = [x for x in list_1 if isinstance(x, str) and 'a' in x]
# print(list_3)

#3 Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

# list_1 = ['cat', 'dog', 'horse', 'cow']
# list_2 = tuple(list_1)
# print(type(list_2))

#4 Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family_1 = tuple(input("Enter members of family 1: ").split(','))
# family_2 = tuple(input("Enter members of family 2: ").split(','))
#
# if len(family_1) > len(family_2):
#     print("family 1 is larger than family 2")
# elif len(family_1) < len(family_2):
#     print("family 2 is larger than family 1")
# else:
#     print("families are equal")

#5 Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    # о вашем любимом фильме.
    # - распечатайте только ключи
    # - распечатайте только значения
    # - распечатайте пары ключ - значение

# a = input("Enter title of movie: ")
# b = input("Enter director of movie: ")
# c = input("Enter year of movie: ")
# d = input("Enter budget of movie: ")
# e = input("Enter main_actor of movie: ")
# f = input("Enter slogan of movie: ")
#
# film = {'title': a, 'director': b, 'year': c, 'budget': d, 'main_actor': e, 'slogan': f}
# print(film.keys())
# print(film.values())
# print(film.items())

#6 Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

#7 Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

# print(set([1, 2, 3, 4, 5, 3, 2, 1]))

#8 Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     # - найдите значения, которые встречаются в обоих множествах
     # - найдите значения, которые не встречаются в обоих множествах
     # - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))

# def sum_mix(arr):
#     sum = 0
#     for i in arr:
#         if type(i) == int:
#             sum += i
#         else:
#             sum += int(i)
#     return sum

# def distinct(seq):
#     return sorted(set(seq))
#
# print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))

# take the second element for sort
# def take_second(elem):
#     return elem[1]


# random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
# sorted_list = sorted(random, key=take_second)

# print list
# print('Sorted list:', sorted_list)

# def convert_palindromes(numbers):
#     arr = [x=1 for x in numbers if x==x.reverse() ]
#     return arr

# def convert_palindromes(numbers):
#     return [str(n) == str(n)[::-1] for n in numbers]
#
#
# print(convert_palindromes([101, 2, 85, 33, 14014]))

# def describe_age(a):
#     s = "kid" if a < 13 else "teenager" if a < 18 else "adult" if a < 65 else "elderly"
#     return f"You're a(n) {s}"
#
#
# print(describe_age(18))