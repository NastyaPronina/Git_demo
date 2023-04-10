# s = "Hello world"
# print(s.replace('e', 'a'))
# print(s.replace("l", "?", 3))
# print(s.count("o"))

# w1 = "1, 2, 3, 4, 5, 6"
# print(w1.split(","))
#
# w2 = w1.split(",")
# print("".join(w1))
# print("? ".join(w1))

# w3 = "123hello   123"
# # print(w3.strip())
# print(w3.strip().strip("123"))

# w4 = "hello world"
# print(w4.find('w', 1, 5))
# print(w4.index("p"))

# w5 = "name world title"
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

# w6 = "qwerty"
# w7 = "Qwerty"
# w8 = "1234tyu"
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())

# w9 = "Qfdgfdgd"
# print(w9.isupper())

# w1 = "01234"
# w2 = "125qweqwe"
# w3 = "0,1"
# print(w1.isdigit())
# print(w2.isdigit())
# print(w3.isdigit())

# a = int(input("Enter digit: "))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} is divisible by 2 and 10")
#     else:
#         print(f"{a} is divisible by 2")
# else:
#     print(f"{a} is not divisible by 2")

# q = int(input("Enter your mark: "))
# if q >= 90:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >= 70:
#     print(3)
# else:
#     print(2)

# number = int(input("Enter digit: "))
# if number < 10:
#     print("single digit")
# elif 10 <= number <= 99:
#     print("two-digit number")
# elif 100 <= number <= 999:
#     print("three-digit number")
# else:
#     print("haven't learnt it yet")

# x, y = 55, 50
# s = x if x > y else y
# print(s)

# value = 1
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print("There is no such digit")

# c = 1
# while c < 5:
#     if c % 2 == 0:
#         print("Chet")
#     else:
#         print("Nechet")
#     c += 1

# value = int(input("Enter digit: "))
# count = 0
# while value != "stop":
#     sum = int(value)
#     count += sum
#     value = input("To continue entering digit, if you want enter stop: ")
# print(f"Sum of digits is equal {count}")

# num = 10
# for i in range(1, num + 1, 2):
#     print(i)

# string_1 = "hellO"
# for i in range(len(string_1)):
#     print(i)
#
# for i in range(len(string_1)):
#     if string_1[i].isupper():
#         print(i, string_1[i])

n = 4
word = "hello"
def repeat_str(repeat, string):
    return repeat * string

print(repeat_str(n, word))