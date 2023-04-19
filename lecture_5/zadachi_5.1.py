# 3 - 1

# def div_con(x):
#     sum_numbers = sum([n for n in x if isinstance(n, int)])
#     sum_str = sum([int(n) for n in x if isinstance(n, str)])
#     return sum_numbers - sum_str
#
#
# print(div_con([9, 3, "7", "3"]))

# 1 Create a class Ghost. Ghost objects are instantiated without any arguments. Ghost objects are given a random
# color attribute of "white" or "yellow" or "purple" or "red" when instantiated

import random
from bisect import bisect_left


# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])
#

# class Ghost(object):
#     def __init__(self):
#         c = {1: "white", 2: "yellow", 3: "purple", 4: "red"}
#         self.color = c[random.randint(1, 4)]
#
# ghost1 = Ghost()
# print(ghost1.color)

# 2 You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a pretty
# efficient system to identify ships with heavy booty on board! Unfortunately for you, people weigh a lot these days,
# so how do you know if a ship is full of gold and not people?

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#     def is_worth_it(self):
#         return self.draft - self.crew * 1.5 > 20

# 3 The following code was thought to be working properly, however when the code tries to access the age of the
# person instance it fails. For this exercise you need to fix the code so that it works correctly.
# Note: the order of the person's full name is first name and last name.

# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + " " + last_name

# 4
# class Block:
#
#     def __init__(self, lst):
#         self.width = lst[0]
#         self.length = lst[1]
#         self.height = lst[2]
#
#     def get_width(self):
#         return self.width
#
#     def get_length(self):
#         return self.length
#
#     def get_height(self):
#         return self.height
#
#     def get_volume(self):
#         return self.width * self.length * self.height
#
#     def get_surface_area(self):
#         return 2 * self.width * self.length + 2 * self.height * self.length + 2 * self.width * self.height

# 5 This kata is about static method that should return different values.
# On the first call it must be 1, on the second and others - it must be a double from previous value.

# class Class:
#     count = 0
#
#     @staticmethod
#     def get_number():
#         result = 2 ** Class.count
#         Class.count += 1
#         return result
#
#
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())

# 6 In this kata, you need to write a function that takes a string and a letter as input and then returns the index
# of the second occurrence of that letter in the string. If there is no such letter in the string, then the function
# should return -1. If the letter occurs only once in the string, then -1 should also be returned.

# def second_symbol(s, c):
#     return s.find(c, s.find(c)+1)
#
# print(second_symbol('Hello world!!!', 'e'))

# 7 Your task is to remove all consecutive duplicate words from a string, leaving only first words entries.

# def remove_consecutive_duplicates(s : str) -> str:
#     s = s.split(" ")
#     lst = [s[0]]
#     for i in range(1, len(s)):
#         if s[i] != lst[-1]:
#             lst.append(s[i])
#     return ' '.join(lst)

# 8 Please write a function that sums a list, but ignores any duplicate items in the list.
# For instance, for the list [3, 4, 3, 6] , the function should return 10.
# def sum_no_duplicates(l):
#     return sum(list(filter(lambda x: l.count(x) == 1, l)))
#
# print(sum_no_duplicates([1, 1, 2, 3]))

# 9 Provided is a function find which accepts two parameters in the following order: array, element and returns
# the index of the element if found and "Not found" otherwise. Your task is to shorten the code as much as possible
# in order to meet the strict character count requirements of the Kata. (no more than 85) You may assume that all
# array elements are unique.

# def find(arr, elem): return arr.index(elem) if elem in arr else 'Not found'
#
# print(find([2, 3, 5, 7, 11], 8))

# 10 Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list ( depending on language ).

# def count_by(x, n):
#     return [i*x for i in range(1, n+1)]
#
# print(count_by(2, 5))

# 11 This kata requires you to write a function which merges two strings together. It does so by merging the end
# of the first string with the start of the second string together when they are an exact match.
# "abcde" + "cdefgh" => "abcdefgh"
# "abaab" + "aabab" => "abaabab"
# "abc" + "def" => "abcdef"
# "abc" + "abc" => "abc"

# def merge_strings(first, second):
#     start = 0
#     stop = len(first)
#     while True:
#         if first[start: len(first)] == second[0:stop]:
#             break
#         else:
#             start = start + 1
#             stop = stop - 1
#     return first[0: start] + second
#
# print(merge_strings('abaab', 'aabab'))



