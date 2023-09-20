# Ticket Class Example except a bit more complex
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

t1 = Ticket('Mark, Smith', 'Opera')
t2 = Ticket('Shuman, Gene', 'Nats Game')

print(t1.eqTick(t2))

print(t1)
print(t2)


def solution(a, signs, b, c):
    output = []
    for i in range(len(a)):
        if signs[i] == '+':
            if a[i] + b[i] == c[i]:
                output.append(True)
            else:
                output.append(False)
        elif signs[i] == '-':
            if a[i] - b[i] == c[i]:
                output.append(True)
            else:
                output.append(False)
    return output
        
