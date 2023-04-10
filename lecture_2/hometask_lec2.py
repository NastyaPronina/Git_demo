# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
import sys

# if max - health <= 0:
#     print('Dead')
# else:
#     print('Alive')

# max = 100
# damage = int(input("Input damage: "))
# while max - damage >= 0:
#     print("Alive")
#     damage = int(input("Input damage: "))
# else:
#     print("Dead")

# Напишите программу, которая проверяет является ли введенное число четным. Если да,
# выведите на экран текст “Четное”, а иначе - “Нечетное”

# num = int(input("Enter digit: "))
# if num%2:
#     print("digit is not even")
# else:
#     print("digit is even")

# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# text = input("Enter text: ")
# n = 5
# for i in range(n):
#     print(text)

# text = input("Enter text: ")
# row = int(input("Enter count: "))
# print((text + '\n') * row)


# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

# try:
#         num1 = int(input("Enter digit 1: "))
#         num2 = int(input("Enter digit 2: "))
# except ValueError:
#         print('You entered not a digit!')
#         sys.exit()
# operator = input("Enter operator: ")
#
#
# if operator == "+":
#         result = num1 + num2
# elif operator == "-":
#         result = num1 - num2
# elif operator == "/":
#         if num2 == 0:
#                 try:
#                         result = num1 / num2
#                 except ZeroDivisionError:
#                         print("Cannot be divided by 0!")
#                 sys.exit()
#         result = num1 / num2
# else:
#         result = num1 * num2
#
# print(f"{num1} {operator} {num2} = {result}")

# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся
# без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка
# на 400, он также считается високосным (1200, 2000)
#
# year = int(input("Enter the year: "))
#
# if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#         print("It is a leap year")
# else:
#         print("Year is not leap")