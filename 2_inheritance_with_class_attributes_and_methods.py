# Task 2

"""
Understand how to use class attributes and class methods alongside inheritance.
Extend the Vehicle class to include a class attribute vehicle_count
and a class method increment_vehicle_count() that increases the count 
every time a new vehicle instance is created. Ensure that both Vehicle 
and Car classes update the vehicle_count appropriately whenever a new 
instance is created. Add a class method get_vehicle_count() that returns 
the current number of vehicle instances.

"""

class Vehicle:
    vehicle_count = 0
        
    def __init__(self, make, model,):
        self.make = make
        self.model = model
        self.increment_vehicle_count()

    def increment_vehicle_count(self):
        Vehicle.vehicle_count += 1

    def get_vehicle_count(self):
        return Vehicle.vehicle_count
        
class Car(Vehicle):
    def __init__(self, make, model, number_of_wheels = 4):
        super().__init__(make,model)
        self.number_of_wheels = number_of_wheels

car = Car("Mercedes-Benz", "CLS")
car1 = Car("Tesla", "Model X")
car2 = Car("BMW", "I8")

print("Number of vehicles:", car.get_vehicle_count())