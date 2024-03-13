# Task 3

"""
Practice method overriding and extend functionality using super().
Add a method start_engine to the Vehicle class that prints "Engine started". 
Override the start_engine method in the Car class to print "Car engine 
started"before calling the Vehicle’s start_engine method using super().

"""

class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
        super().start_engine()

vehicle = Vehicle()
vehicle.start_engine() 
print()

car = Car()
car.start_engine()