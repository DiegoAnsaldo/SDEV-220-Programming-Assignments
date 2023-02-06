# I was unsure how you wanted this homework to be formatted, so I am doing my best here. Please let me know if I was supposed to
# do it differently, and if I missed that instruction somewhere, I apologise.

import math

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return math.dist(self.coor1, self.coor2)
    
    def slope(self):
        return ((self.coor1[1] - self.coor2[1])/(self.coor1[0] - self.coor2[0]))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

# Output that I didn't want to take up space unnesesarily
# print(li.distance())
# print(li.slope())


# Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (math.pi * (self.radius ** 2) * self.height)
    
    def surface_area(self):
        return ((2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2)))

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())