# 1. Given an array/list [] of integers , Construct a product array Of same size Such That prod[i]
# is equal to The Product of all the elements of Arr[] except Arr[i].
import math


# from functools import reduce
# from math import prod
# from operator import mul
#
# def product_array(numbers):
#     tot = reduce(mul, numbers)
#     return [tot//n for n in numbers]
#
# def product_array1(numbers):
#     return [prod(numbers)/i for i in numbers]
#
# print(product_array([3, 27, 4, 2]))

# 2. The point is that a natural number N (1 <= N <= 10^9) is given. You need to write a function which
# finds the number of natural numbers not exceeding N and not divided by any of the numbers [2, 3, 5].

# def real_numbers(n):
#     count = 0
#     for i in range(1, n + 1):
#         if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and n != 0:
#             count += 1
#     return count
#
# def real_numbers1(n):
#     lst = list(range(1, n + 1))
#     return len(list(filter(lambda x: (x % 2 != 0) and (x % 3 != 0) and (x % 5 != 0), lst)))
#
# print(real_numbers1(40))

# 3. Implement a function hyperfact(num) that takes a positive integer num and returns the hyperfactorial of it.
# In order for your answer not to be too messy (hyperfactorial of 100 is 9015 digits long) give the answer
# modulo 1000000007.

# def hyperfact(num):
#     res = 1
#     for m in range(1, num + 1):
#         res = (res * pow(m, m, 1000000007)) % 1000000007
#     return res
#
# print(hyperfact(100))

# 4. Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout and Cell phone keypad's layout. Solve the horror of unstandardized keypads by providing
# a function that converts computer input to a number as if it was typed on a phone.
# Example:
# "789" -> "123

# def computer_to_phone(numbers):
#     return numbers.translate(str.maketrans('123789', '789123'))
#
# print(computer_to_phone("919"))

# 5. When provided with a String, capitalize all vowels
# For example:
# Input : "Hello World!"
# Output : "HEllO WOrld!"

# def swap(st):
#   tr = str.maketrans('aeiou', 'AEIOU')
#   return st.translate(tr)
#
# print(swap("Monday"))

def keep_order(ary, val):
    element = ary[0]
    for i in ary:
        if i >= val:
            element = ary.index(element)
    return element


print(keep_order([1, 2, 3, 4, 7], 5))
