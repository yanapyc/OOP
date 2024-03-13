# Task 4

"""
Demonstrate understanding of multiple inheritance and MRO.
Create a new class ElectricVehicle with its own __init__ method that 
includes an attribute battery_capacity. Create a subclass ElectricCar 
that inherits from both Car and ElectricVehicle. Make sure to properly 
initialize all parent classes and deal with potential inheritance issues. 
Explain how Python resolves method calls (like __init__) in the context 
of multiple inheritance and how the MRO can be inspected using the .__mro__ 
attribute or the mro() method.

"""

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, number_of_wheels = 4):
        super().__init__(make, model)
        self.number_of_wheels = number_of_wheels

class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity


class ElectricCar(Car, ElectricVehicle):
    def __init__(self,make, model, number_of_wheels, battery_capacity):
        Car.__init__(self,make, model,number_of_wheels)
        ElectricVehicle.__init__(self,battery_capacity)

electric_car = ElectricCar("Tesla", "X", 4, 100)
print("Make:", electric_car.make)
print("Model:", electric_car.model)
print("Number_of_wheels:", electric_car.number_of_wheels)
print("Battery Capacity:", electric_car.battery_capacity)