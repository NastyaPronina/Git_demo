# 1 Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are
# grouped and groups are space-separated (see sample below)
# input: 'CodeWars'
# output 'CdWr oeas'

# def sort_my_string(s):
#     result1 = ""
#     result2 = ""
#     for i in range(len(s)):
#         if i%2 == 0:
#             result1 += s[i]
#         else:
#             result2 += s[i]
#     return f"{result1} {result2}"
#
#
# def sort_my_string1(s):
#     return s[::2] + ' ' + s[1::2]
#
# print(sort_my_string("CodeWars"))

#2 Cats and shelves
# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the
# shelf directly above its head), according to the illustration:

# def solution(start, finish):
#     return (finish - start)%3 + (finish - start)//3
#
# print(solution(2,4))

# 3 Between Extremes
# Given an array of numbers, return the difference between the largest and smallest values.

# def between_extremes(numbers):
#     return max(numbers) - min(numbers)
#
# print(between_extremes([1, 1]))

# 4 Between Extremes
# Given an array of numbers, return the difference between the largest and smallest values.
# For example:
# [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).
# [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1)

# between_extremes = lambda numbers: max(numbers) - min(numbers)
# print(between_extremes([1, 5]))

# 5 Sum even numbers
# Complete the function that takes a sequence of numbers as single parameter. Your function must return the sum of the
# even values of this sequence.
# The input is a sequence of numbers: integers and/or floats.

# def sum_even_numbers(seq):
#     # return sum(x for x in seq if x%2 == 0)
#     return lambda x: sum(x if x%2 else 0)
#
# sum_even_numbers1 = lambda x: sum(i for i in x if i%2 == 0)
#
# print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 6 Write a program that outputs the top n elements from a list.

# def largest(n, xs):
#     lst = []
#     xs.sort(reverse=True)
#     for i in range(n):
#         lst.append(xs[i])
#     return lst[::-1]
#
# def largest1(n, xs):
#     return sorted(xs)[-n:]

# def largest2(n, xs):
#     return (sorted(xs, reverse=True)[0:n])[::-1]
#
# print(largest2(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

# 7
def give_change(amount):
    lst = [100, 50, 20, 10, 5, 1]
    arr = [0, 0, 0, 0, 0, 0]
    for i in range(len(lst)):
        arr[i] = amount // lst[i]
        amount -= lst[i]*arr[i]
    return arr[::-1]

print(give_change(365))