# LISTS
# Create a list: option 1
# my_list = [1, "hello", 2.4, True, None]
#
# sentence = "Python is awesome"
# print(sentence.split(" "))
#
# print(my_list[-1])

# print('Before', my_list)
# print(id(my_list))
# my_list[0] = 25
# print('After', my_list)
# print(id(my_list))

# my_list.append(sentence)
# print(my_list)
# print(len(my_list))
#
# my_list.insert(0, sentence)
# print(my_list)
# print(len(my_list))
#
# print(my_list.count(1))

# print(my_list.index(None))

# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [1, 2]]]
# print(sum(my_list1))
# print(max(my_list1))
# print(my_list1[-1])
# print(my_list1[-1][-1])
# print(my_list1[-1][-1][1])
# my_list1.reverse()
# print(my_list1)

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num * 2)

# new_l = [i for i in numbers if i % 2]
# print(new_l)

# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))
#
# my_tuple = (1, True, "name", None, "name", "name", 25)
# print(my_tuple)
#
# name = "Mark",
# print(name)

# my_tuple = ("apple", "banana", "cat")
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)
#
# letters = list(my_tuple)
# letters[0] = "ananas"
# print(letters)

# my_tuple = (1, True, "name", None, "name", "name", 25)
# print(my_tuple.index("name"))
# print(my_tuple.count("name"))

# my_tuple = (1, "name", None, "name", "name", 25)
# result = tuple([item for item in my_tuple if isinstance(item, int)])
# print(result)
#
# print(f"Sum is: {sum(result)}")
# print(f"Min is: {min(result)}")
# print(f"Max is: {max(result)}")
# print(f"Lenght of my_tuple is: {len(my_tuple)}")
# print(f"Lenght of result is: {len(result)}")

# for (index, item) in enumerate(my_tuple):
#     print(index, item)

# i = 0
# while i < len(my_tuple):
#     print(i, my_tuple[i])
#     i += 1

# fruits = ("apple", ["ananas", "mango"], "melon")
# print(fruits)
# fruits[1][0] = 'cherry'
# print(fruits)

# a = 5
# b = 10
# a, b = b, a
# print(f"a = {a}")
# print(f"b = {b}")

# def sum_it(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total += num
#     return total
# print(sum_it(4, 5, 10, 6, 20))

# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append(item * item)
#     return l
#
# print(func(2, 5, 6, 8, 10))

# my_dict = {}
# print(type(my_dict))

# my_dict = {
#     'name': 'Anna',
#     'surname': 'Pavlova',
#     'age': 30,
#     'department': 'IT'
# }
#
# print(my_dict)
# print(id(my_dict))
# print(id(my_dict))
# print(my_dict["name"])
# print(my_dict['name'])
# my_dict['name'] = 'Volha'
# print(my_dict)
# print(id(my_dict))
# print(len(my_dict))
# my_dict["salary"] = 5000
# print(my_dict)
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('salary', 'Not found'))

# keys = ['name', 'salary', 'department']
# values = ['Alex', 50000, 'HR']
# employee = dict(zip(keys, values))
# print(employee)

# employee1 = dict(name='John', position='developer', salary=20000, department='IT')
# print(employee1)

# my_set = {'name', 'surname', 'salary'}
# my_list = [1, 8, 2, 1, 5, 8, 9]
# print(set(my_list))

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))
# print(set1)
# print(id(set1))
# set1.remove(1)
# set1.add(8)
# print(set1)

# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)

set1 = {1, 2, 3, 'one', 'ten', 6}
