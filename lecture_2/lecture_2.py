# compare = 3 <= 4
# print(compare)
import sys

# x = 6
# print(x > 3 and not x < 8)
# print(x > 3 and not x > 8)

# if x != 5:
#     print('Correct')
# else:
#     print('Incorrect')

# num = 1
# if num == 5:
#     print('five')
# elif num > 5:
#     print('num more than five')
# else:
#     print('num less than five')

# age = int(input('Please, enter your age: '))
# if age >= 18:
#     print("Welcome")
# else:
#     print("Go home, baby")

# try:
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
# except ValueError:
#     print('You entered not a digit!')
#     sys.exit()
# operator = input('Operator: ')
# if (num2 == 0 and operator == "/") or num1 > 5 :
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('Cannot be divided by 0!')
# else:
#     result = num1 * num2
#     print(f"Result = {result}")

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# message = 'Hello'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)

# for i in range(6):
#     print(i)
# for i in range(1, 6, 2):
#     print(i)

# for i in "Hello":
#     print(i)

# message = ""
# if message:
#     print(message)
# else:
#     print("The string is empty")

# num = 6
# if num % 2:
#     print("Not even")
# else:
#     print(" Even")

def num (num1, num2):
    return num1 - num2

print(num(10, 5))