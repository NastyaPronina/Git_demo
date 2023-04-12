class Car:

    transmission = "mechanical"

    def __init__(self, color, wheels, brand, power):
        self.color = color
        self.wheels = wheels
        self.__brand = brand
        self.power = power


    def drive(self):
        return "I can drive!"

    def get_brand(self):
        return f"The name of the car brand is {self.__brand}"

    def set_brand(self, new_brand):
        self.__brand = new_brand


class Volvo(Car):

    def __init__(self, color, wheels, brand, power, model):
        super().__init__(color, wheels, brand, power)
        self.model = model

    def drive(self):
        return "I can drive fast!"

    def speed_up(self):
        return "I can speed up in 2 sec to 100 km/h"


car1 = Car("black", 4, "shevralet", 250)
print(car1.drive())
print(car1.transmission)
print(car1.get_brand())
print(car1.__dict__)
car1.set_brand("bmw")
print(car1.__dict__)

car2 = Volvo("white", 4, "volvo", 280, "v100")
print(car2.drive())
print(car2.transmission)
print(car2.get_brand())
print(car2.__dict__)