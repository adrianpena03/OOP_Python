# OOP Notes 1 - Basics

class Point(object):
    def __init__(self, x, y): # self refers to objects within this attribute, ALSO A METHOD
        self.x = x # Attributes
        self.y = y
    def get_coordinates(self):
        return "(" + str(self.x) + " , " + str(self.y) + ")"
    
p1 = Point(3, 4) # Creates new object of type Point and pass 3 and 4 to the __init__ constructor method
p2 = Point(0, 0)

# print(p1.x)
# print(p2.y)
# print(p1.get_coordinates())
# print(p2.get_coordinates())

# ------------------------------------

class Date:
    def __init__(self, month, day, year, descr):
        self.month = month
        self.day = day
        self.year = year
        self.descr = descr

    def __str__(self): # str method --- idk what it does yet
        monthXlate = {'09': 'September', '10': 'October', '11': 'November'}
        return monthXlate[self.month] + ' ' + self.day + ', ' + self.year


    def getDate(self):
        print(self.month + '/' + self.day + '/' + self.year + '/' + self.descr)



d1 = Date('09', '06', '2023', 'Today') # Object of type 'Date'
d2 = Date('09', '07', '2023', 'Tomorrow')

print(d1) # How does this use __str__ method? why not getDate?
d1.getDate()

# -------------------------------------

# try on my own

class Ticket():
    def __init__(self, serialNumber, custer_name, event):
        self.serialNumber = serialNumber
        self.custer_name = custer_name
        self.event = event

    def __str__(self):
        return str(self.serialNumber) + ' - ' + self.custer_name + ' - ' + self.event # why say self.serialNumber when we put it as "serialNumber" in init method

    def getSerial(self):
        return self.serialNumber
    

t1 = Ticket(100, 'Mark Smith', 'Opera')
t2 = Ticket(200, 'Shuman', 'Nats Game')

print(t1)
print(t2.getSerial)

