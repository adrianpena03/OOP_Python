class Calendar:
    def __init__(self, name, descr = 'Default'):
        # Calendar class - container class for date objects
        self.name = name
        self.descr = descr
        self.dates = []

    def __str__(self):
        return self.name + ' - ' + self.descr
    
    def addDate(self, d_obj):
        # adds date object to calendar, expects input param, returns false if d_obj is not a date, otherwise True
        if not isinstance(d_obj, Date):
            return False
        return True
    
    def showDates(self):
        for d in self.dates: # missing the class Date code. by doing self.dates, it goes into date class and returns the string method
            print(d)

# ---------------------------------------
# Containerize stuff

class Ticket():
    venue = 'Kennedy Center'
    ticketCount = 1
    def __init__(self, cust_name, event):
        self.serialNum = Ticket.ticketCount
        Ticket.ticketCount += 1
        self.cust_name = cust_name
        self.event = event

    def __str__(self):
        return ('\nName: ' + self.cust_name + 
                '\nSerial Number: ' + str(self.serialNum) + 
                '\nEvent: '+ self.event + 
                '\nVenue: ' + Ticket.venue)

    def getSerial(self):
        return self.serialNumber
    
    def eqTick(self, tobj):
        if self.cust_name == tobj.cust_name and self.serialNum == tobj.serialNum and self.event == tobj.event:
            return True
        return False

class Scalp:
    def __init__(self, name):
        self.name = name
        self.tickList = []

    def addTick(self, t_obj):
        if isinstance (t_obj, Ticket):
            self.tickList.append(t_obj)
            return True
        return False
    
    def printTicks(self):
        for t in self.tickList:
            print(t)

s1 = Scalp('Scalper Adrian')
s1.addTick(Ticket('Adrian', 'Demo Derby'))


print(s1)