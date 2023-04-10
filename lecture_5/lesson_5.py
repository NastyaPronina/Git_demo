class Dog:

    biology_class = "Animal"

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color


    def run(self):
        return "I can run!"

    def get_name(self):
        return f"Hello! My name is {self.__name}"

    def set_name(self, new_name):
        self._name = new_name


dog1 = Dog("Bobik", 3, "brown")
# print(dog1.biology_class)
# print(dog1.name)
# print(dog1.get_name())
# print(dog1.weight)

dog2 = Dog("Rex", 7, "Black")
print(dog2.biology_class)
# print(dog2.get_name())
print(dog2.set_name("Snoopy"))
# print(dog2.get_name())
# print(dog2.__name)
print(dog2.__dict__)
print(dog2._Dog__name)
# dog2.name = "Snoopy"

# print(dog2.get_name())
# print(dog2.__dict__)


class Pitbull(Dog):

    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def run(self):
        return "I can run fast!"

    def give_a_paw(self):
        return "I can give a paw!"


dog3 = Pitbull("Lassie", 8, "Black", "type1")
# print(dog3.get_name())
# print(dog3.give_a_paw())
# print(dog3.passport)
# print(dog2.run())
# print(dog3.run())
# print(dog2.__dict__)