from datetime import *
# 1. Write a function that takes a string of parentheses,
# and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
from functools import reduce


# def valid_parentheses(paren_str):
#     while "()" in paren_str:
#         paren_str = paren_str.replace("()", "")
#         return True if paren_str == "" else False
#
#
# print(valid_parentheses("())(()"))

# 2. Your task is to find the nearest square number

# def nearest_sq(n):
#     return round(n**0.5)**2
#
# print(nearest_sq(111))

# 3. Please write a function that sums a list, but ignores any duplicate items in the list.

# def sum_no_duplicates(l):
#     return sum(list(filter(lambda x: l.count(x) == 1, l)))
#
# print(sum_no_duplicates([3, 4, 3, 6]))

# 4. My washing machine uses water amount of water to wash load. For each single item of clothes
# above the load, the washing machine will use 10% more water (multiplicative) to clean.
# For example, if the load is 10, the amount of water it requires is 5 and the amount of clothes
# to wash is 14, then you need 5 * 1.1 ^ (14 - 10) amount of water.

# def how_much_water(water, load, clothes):
#     if clothes > load * 2:
#         return "Too much clothes"
#     if clothes < load:
#         return "Not enough clothes"
#     result = water * 1.1 ** (clothes - load)
#     return round(result, 2)

# or more elegant solution:

# def how_much_water1(water, load, clothes):
#     return "Too much clothes" if load > 2*clothes else "Not enough clothes" if clothes < load else round(water * 1.1 ** (clothes - load))

# using lambda:

# how_much_water2 = lambda w, l, c: "Not enough clothes" if c < l else "Too much clothes" if c > l*2 else round(w*1.1**(c - l))
#
# print(how_much_water2(5, 10, 18))

# 5. https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
# There is a bus moving in the city which takes and drops some people at each bus stop.
# You are provided with a list (or array) of integer pairs. Elements of each pair represent
# the number of people that get on the bus (the first item) and the number of people that get
# off the bus (the second item) at a bus stop.
# Your task is to return the number of people who are still on the bus after the last bus stop

# def number(bus_stops):
#     result = 0
#     for i in bus_stops:
#         result += i[0] - i[1]
#     return result
#

# def number1(bus_stops):
#     return sum(map(lambda i: i[0] - i[1], bus_stops))

#
# def number2(bus_stops):
#     result = 0
#     for i, j in bus_stops:
#         result += i - j
#     return result

# def number3(bus_stops):
#     return sum([stop[0] - stop[1] for stop in bus_stops])
#
# print(number1([[10, 0], [3, 5], [5, 8]]))

# 6. https://www.codewars.com/kata/5a19226646d843de9000007d/train/python
# Complete the function that counts the number of unique consonants in a string (made up of printable ascii characters).
# Consonants are letters used in English other than "a", "e", "i", "o", "u".

# def count_consonants(text):
#     text1 = set(text.lower())
#     l = []
#     for i in text1:
#         if i not in "aeiou" and i.isalpha():
#             l.append(i)
#     return len(l)
#
#
# def count_consonants1(text):
#     return len({i for i in text.lower() if i not in "aeiou" and i.isalpha()})
#
# def count_consonants2(text):
#     return len({i for i in text.lower() if i in "bcdfghjklmnpqrstvwxyz" and i.isalpha()})
#
# print(count_consonants2("abcdefghijklmnopqrstuvwxyz"))

# 7. https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python

# def alias_gen(f_name, l_name):
#     FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
#     SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}
#     if f_name[0].isalpha() and l_name[0].isalpha():
#         return f"{FIRST_NAME.get(f_name[0].title())} {SURNAME.get(f_name[0].title())}"
#     return "Your name must start with a letter from A - Z."
#
#
# print(alias_gen('Ahima', 'Billund'))

# 8. https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/train/python
# Given an unsorted array of integers, find the smallest number in the array, the largest number in the array,
# and the smallest number between the two array bounds that is not in the array.
# For instance, given the array [-1, 4, 5, -23, 24], the smallest number is -23, the largest number is 24, and
# the smallest number between the array bounds is -22.

# def min_min_max(arr):
#     a, b = min(arr), max(arr)
#     return [a, next(i for i in range(a + 1, b) if i not in arr), b]
#
#
# def min_min_max1(arr):
#     a1 = sorted(arr)
#     lst = [a1[0], None, a1[-1]]
#     num = a1[0] + 1
#     while num in a1[1: -1]:
#         num += 1
#     return [a1[0], num, a1[-1]]
#
# print(min_min_max([1, 3, -3, -2, 8, -1]))

# 9. You're writing code to control your town's traffic lights. You need a function to handle each change from green,
# to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a
# string representing the state the light should change to.
# For example, when the input is green, output should be yellow.

# def update_light(current):
#     return {"green": "yellow", "yellow": "red", "red": "green"}[current]

# print(update_light("red"))

# 10. I have a cat and a dog.
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

# def human_years_cat_years_dog_years1(n):
#     return [n, 24+(n-2)*4 if (n != 1) else 15, 24+(n-2)*5 if (n != 1) else 15]
#
# print(human_years_cat_years_dog_years1(10))

# 11. Complete the square sum function so that it squares each number passed into it and then sums the
# results together.

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
#
#
# print(square_sum([-1, -2]))

# 12. Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# "4",  "5" --> "9"
# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))
#
# print(sum_str("", ""))

# 13. Create a method to see whether the string is ALL CAPS.
# def is_uppercase(inp):
#     return inp.upper()==inp
#
# print(is_uppercase("hello I AM DONALD"))

# 14. Clear the given text from digits
# def string_clean(s):
#     return "".join(x for x in s if not x.isdigit())
#
# print(string_clean("(E3at m2e2!!)"))

# 15. Remove an exclamation mark from the end of a string.

# def remove(s):
#     return s[:-1] if s.endswith('!') else s
#
# print(remove("hello!!"))

# 16. Write a function which removes from string all non-digit characters and parse the remaining
# to number. E.g: "hell5o wor6ld" -> 56

# def get_number_from_string(string):
#     return int("".join(x for x in string if x.isdigit()))
#
# print(get_number_from_string("1"))

# 17. If you pass the list of your favourite animals to the function, you should get the list of the
# animals with orderings and newlines added.

# def list_animals(animals):
#     return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))

# 18. Consider an array/list of sheep where some sheep may be missing from their place. We need a function
# that counts the number of sheep present in the array (true means present).

# def count(sheeps):
#     return sheeps.count(True)

# 19. Determine if the baby will be a boy or a girl depending on the resulting chromosomes

# def chromosome_check(sperm):
    # return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')

