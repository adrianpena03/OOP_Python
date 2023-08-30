class Point(object):
    def __init__(self, x, y): # self refers to objects within this attribute
        self.x = x
        self.y = y
    def get_coordinates(self):
        return "(" + str(self.x) + " , " + str(self.y) + ")"
    
p1 = Point(3, 4) # Creates new object of type Point and pass 3 and 4 to the __init__ constructor method
p2 = Point(0, 0)

print(p1.x)
print(p2.y)
print(p1.get_coordinates())
print(p2.get_coordinates())

