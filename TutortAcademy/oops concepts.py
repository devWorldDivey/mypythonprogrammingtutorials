"""
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"The {self.make} {self.model} is now driving")
class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    def drive(self):
        print(f"The {self.make} {self.model} with {self.num_doors} doors is now driving")

my_vehicle = Vehicle("Ford","F-150")
my_vehicle.drive()

my_car = Car("Toyota","Camry",4)
my_car.drive()
"""
"""
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Generic animal sound")
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name,"cat")
        self.breed = breed
    def make_sound(self):
        print("Meow")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,"dog")
        self.breed =breed
    def make_sound(self):
        print("woof")

my_cat = Cat("Wiskers","Siamese")
my_dog = Dog("Fido","Golden Retriever")
print(my_dog.name)
print(my_cat.name)
"""

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(f"Hi name is {self.name} and I am {self.age} years old.I am in grade {self.grade}")


p1 = Person("Alice", 30)
p1.introduce()
p2 = student("Bob", 12, 6)
p2.introduce()
"""
class BankAccount:
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit of amount{amount: .2f} successful. New balance is {self.balance:.2f}")
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount:.2f} successful. New balance is {self.balance:.2f}")
    def get_balance(self):
        print(f"Current balance is {self.balance:.2f}")
account1 = BankAccount("Alice")
account1.deposit(1000)
account1.withdraw(500)
account1.get_balance()
account2 = BankAccount("Bob",500)
account2.deposit(2000)
account2.withdraw(1000)
account2.get_balance()