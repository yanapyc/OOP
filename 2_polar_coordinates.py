# Task 5

"""
Implement operator overloading to add two points represented in polar coordinates.
Create a class Polar that represents a point on the plane using polar coordinates 
(radius and angle in degrees). Implement the __init__ and __repr__ methods for the 
Polar class. The __init__ method should initialize radius and angle attributes, 
while __repr__ should return a string representation of the polar coordinate.
Overload the + operator to enable addition of two Polar objects. This involves:Converting 
polar coordinates to rectangular (Cartesian) coordinates for each point. Adding the 
respective X and Y coordinates of the two points. Converting the resulting point back 
to polar coordinates and returning a new Polar instance with these coordinates.

"""

import math

class Polar:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def __repr__(self):
        return f"Radius: {self.radius}, Angle: {self.angle}"

    def __add__(self, other):
        x1 = self.radius * math.cos(math.radians(self.angle))
        y1 = self.radius * math.sin(math.radians(self.angle))

        x2 = other.radius * math.cos(math.radians(other.angle))
        y2 = other.radius * math.sin(math.radians(other.angle))

        x = x1 + x2
        y = y1 + y2

        radius_polar = math.sqrt(x**2 + y**2)
        angle_polar = math.degrees(math.atan2(y,x))

        return Polar(radius_polar, angle_polar)


polar1 = Polar(3, 60)
polar2 = Polar(4, 90)

polar_sum = polar1 + polar2

print("Sum of two coordinates:\n",polar_sum)