# Task 1

"""
Create a simple class hierarchy that demonstrates basic 
inheritance and the use of super() in __init__ methods.
Define a base class Vehicle with __init__ method initializing
attributes make and model . Create a subclass Car that inherits
from Vehicle and adds an attribute number_of_wheels with a default
value of 4. Ensure the subclass calls the __init__ method of Vehicle
using super(). Implement a __repr__ method in both classes to nicely
format their information.

"""

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'{self.make} {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, number_of_wheels = 4):
        super().__init__(make,model)
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return f'{self.make} {self.model} has a {self.number_of_wheels} wheels'
    
car = Car("FERRARI", "Portofino")
print(car)