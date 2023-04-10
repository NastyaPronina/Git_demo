# def multi(a, b):
#     return a * b
#
#
# num = multi(5, 10) + 10
# print(num)
#
# def say_hello():
#     print("Hello")
#
# say_hello()
#
# def check_even(a):
#     lst = []
#     for i in range(a):
#         if i % 2 == 0:
#             lst.append("yes")
#         else:
#             lst.append("no")
#     return lst
#
#
# print(check_even(10))
#
# for i in range(15):
#     check_even(i)

# def fun():
#     s = "Hi"
#     print(f"First {s}")
#
# s = "Hello"
# fun()

# def multi():
#     x = 10
#
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
#
# y = 5
# multi()

# def multi(a, b):
#     print(a * b)
#
# multi(2, 5, 11)

# a, b, *c = [1, 'Hello', 3.5, True]
# print(a, b, c)

# def fun(*nums):
#     print(nums)
#
#
# a = {True, 51, "Hello", 44}
# fun(*a)

# a = "Hello, {}!".format('Vasia')
# print(a)

# lst = ['a', 'b', 'c']
# a = "{2}, {1}, {0}".format(*lst)
# print(a)

# def fun(*args):
#     print(args)
#
#
# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6]
# c = {1: '12',
#      2: '15',
#      3: '20'}
# fun(a)

# def fun(*args):
#     print(args)
#
#
# a = "True, 51, 'Hello', 7.8"
# fun(a)

# def fun(*args):
#     s = 0
#     print(args)
#     for i in args:
#         s += i
#     print(s)
#
#
# a = (1, 4, 7, 19, 10, 12)
# fun(*a)

# def return_dict(*args, **kwargs):
#     print(kwargs)
#     print(args)
#
#
# return_dict(1, 2, 3, a=2, b=4, c=6)
# # return_dict(1, 2, 3)

# def fun(x):
#     # if x < 10:
#         print(x)
#         fun(x + 1)
#
# fun(1)

# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n - 1) * n
#
# print(fact(5))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(7))

# def fun(x):
#     return x**3
#
# power = lambda x: x**3
# print(power(3))
#
# print(fun(3))

# s = lambda x: x*x if x > 5 else x
# print(s(4))

# a = [34, 67, 2, 54, 9]
#
# a.sort(key=lambda x: x % 2) # even elements first
# print(a)

# print(sorted(a, key=lambda x: x % 2))
# print(sorted(a, key=lambda x: x % 10))

# a = ['hello', 'aaa', 'bbb', 'xxx']
# print(sorted(a))

# a = [(1, 2), (2, 1), (3, 3)]
# b = sorted(a, key=lambda x: x[1])
# print(*b)

# a = ['qqq 23', 'qqq 12', 'rrr 8']
# print(sorted(a, key = lambda x: x.split()[1]))

# a = '1 2 3 4 5'
# b = list(a)
# b1 = a.split()
# b2 = list(map(int, a.split()))
# print(b2)

# def fun_n(x):
#     return x**2
#
#
# def fun(x):
#     return x**3
#
#
# a = [-1, 3, -5, 7]
# a1 = list(map(str, a))
# print(a1)
# c = list(map(abs, a))
# print(c)
# d = list(map(fun_n, a))
# print(d)

# a = [12, 5, 7, 3, 2, 0, -5]
# a1 = list(filter(lambda x: x > 5, a))
# print(a1)