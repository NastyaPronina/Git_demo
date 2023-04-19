# class Car:
#     name = "Priora"
#     make = "Lada"
#     age = 2020
#
#
#     def start(self, name, make = "Audi"):
#         self.name = name
#         self.make = make
#         print(f"У машины {self.make} {self.name} заведен двигатель")
#
#
#     def get_age(self):
#         print(f"Машина {self.make} {self.name} {self.age} выпуска")


    # def stop(self):
    #     print("stop the engine")


# car1 = Car()
# car2 = Car()
# car1.start("Q7")
# print(type(car1))
# print(car1.name)
# print(car1.make)
# print(car1.age)
# car1.start()
# print(Car.name)
# print(Car.__dict__)
#
# a1 = Car()
# print(getattr(Car, "name"))
# Car.make = "mercedez"
# print(getattr(Car, "make"))
# setattr(Car, "y", 1000)
# print(Car.__dict__)
# del Car.y
# print(Car.__dict__)

# class Cat:
#
#     def __init__(self):
#         print("Hello")

# cat1 = Cat()


# class HockeyPlayer:
#
#     def __init__(self, name, surname, goal=0, assist=0):
#         self.name = name
#         self.surname = surname
#         self.goal = goal
#         self.assist = assist
#
#
#     def goals(self, goal=0):
#         self.goal = goal
#
#
#     def all_assist(self, assist=0):
#         self.assist = assist
#
#     def statistics(self):
#         print(f"HockeyPlayer Name: {self.name} {self.surname}")
#         print(f"Goals: {self.goal}")
#         print(f"Assist: {self.assist}")


# ovechkin = HockeyPlayer("Alexandr", "Ovechkin")
# ovechkin.goals(700)
# ovechkin.all_assist(500)
# ovechkin.statistics()
#
# vin = HockeyPlayer("Vinsent", "Lekavale")
# vin.goals(500)
# vin.all_assist(600)
# vin.statistics()


# class Person:
#
#     def can_breathe(self):
#         print("Я дышу")
#
#
#     def can_walk(self):
#         print("Я хожу")
#
#     def can_sleep(selfself):
#         print("Я сплю")
#
#
# class Teacher(Person):
#
#     def can_breathe(self):
#         print("Учитель дышит")
#
#
#     def can_teach(self):
#         print("Я учу")
#
#
#     def can_check(self):
#         print("Я проверяю")
#
# t1 = Teacher()
# t1.can_sleep()
# t1.can_walk()
# t1.can_breathe()
# t1.can_teach()
#
# p1 = Person()
# print(issubclass(Teacher, Person))
# print(issubclass(Person, object))

# class Animals:
#     def can_breathe(self):
#         print("Могу дышать")
#
# class Dogs:
#     def can_bark(self):
#         print("Wow-wow")
#
# class Beagle(Animals, Dogs):
#     def can_sleep(self):
#         print("I'm sleeping")
#
# b1 = Beagle()
# b1.can_breathe()
# b1.can_bark()
# print(Beagle.__mro__)

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_info(self):
        print(f"Cat name: {self.name}, cat age: {self.age}")

    def speak(self, sound):
        self.sound = sound
        print(f"Cat {self.name} said {self.sound}")


cat1 = Cat("Sam", 5)
cat1.get_info()
cat1.speak("Meu")