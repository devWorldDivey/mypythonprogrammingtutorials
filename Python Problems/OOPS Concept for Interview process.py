#Class is a blueprint for creating objects
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
#Object is instance of a class
my_car = Car("Honda","Civic",2022)
#inheritance - Feature of OOPS to create a new class which is modified version of new class
class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery_size = battery_size
    def charge(self):
        print("The car is charging.")
#Polymorphism - single interface to represent multiple classes
class Pet:
    def speak(self):
        pass
    def Cat(Pet):
        def speak(self):
            return "Meow"
    def Dog(Pet):
        def speak(self):
            return "Woof"