class Ticket(object):    # superclass
    """ Ticket Class - getSerial, toString methods """
##    ticketCount = 0
    def __init__(self, event, name, date, agent):
        self.event = event
        self.name = name
        self.date = date
        self.agent = agent
    def getAgent(self):
        return self.agent
    def __str__(self):
        return ('\nEvent:  ' + self.event + '\nCustomer: ' + self.name +
                '\nDate:   ' + self.date + '\nAgent:   ' + self.agent)

class NatsTick(Ticket):
    ticketCount = 0
    def __init__(self, event, name, date, agent, venue, opponent):
        super().__init__(event, name, date, agent)
        NatsTick.ticketCount += 1
        self.serialNumber = NatsTick.ticketCount
        self.venue = venue
        self.opponent = opponent
    def __str__(self):
        return ((super().__str__()) + '\nVenue:    ' + self.venue +
                 '\nOpponent:   ' + self.opponent + '\nSerial Number: ' +
                 str(self.serialNumber))

class FlightTick(Ticket):
    """FlightTick creates a ticket object for an airline flight """
    ticketCount = 1
    def __init__(self,event, name, date, agent, airport, destination, dep):
        super().__init__(event, name, date, agent)
        self.serialNumber = FlightTick.ticketCount
        FlightTick.ticketCount += 1
        self.airport = airport
        self.destination = destination
        self.departureTime = dep

    def __str__(self):
        return ((super().__str__()) + '\nFrom:    ' + self.airport +
                 '\nto:   ' + self.destination + '\nDeparting at: ' +
                 self.departureTime + '\nSerial Number: ' + str(self.serialNumber))        

# Global code: Create three objects for demo ---------------------------

input('\nHit "Enter" to create 1 Ticket, 1 NatsTick, and 1 FlightTick object')
t1 = Ticket('GMU Basketball', 'Ken Ball', '03/01/2024', 'GMU TicketMaster')
nt1 = NatsTick('ballgame', 'GRS', 'April 5, 2024', 'MRizzo', 'Nats Park', 'Mets')
ft1 = FlightTick('Flight', 'Anthony', 'November 27, 20230', 'ElizabethR',
                 'Washington Dulles(IAD)', 'San Francisco','7:15 pm')

print('\nObjects t1, nt1, and ft1 created \n')
class Ticket(object):    # superclass
    """ Ticket Class - getSerial, toString methods """
##    ticketCount = 0
    def __init__(self, event, name, date, agent):
        self.event = event
        self.name = name
        self.date = date
        self.agent = agent
    def getAgent(self):
        return self.agent
    def __str__(self):
        return ('\nEvent:  ' + self.event + '\nCustomer: ' + self.name +
                '\nDate:   ' + self.date + '\nAgent:   ' + self.agent)

class NatsTick(Ticket):
    ticketCount = 0
    def __init__(self, event, name, date, agent, venue, opponent):
        super().__init__(event, name, date, agent)
        NatsTick.ticketCount += 1
        self.serialNumber = NatsTick.ticketCount
        self.venue = venue
        self.opponent = opponent
    def __str__(self):
        return ((super().__str__()) + '\nVenue:    ' + self.venue +
                 '\nOpponent:   ' + self.opponent + '\nSerial Number: ' +
                 str(self.serialNumber))

class FlightTick(Ticket):
    """FlightTick creates a ticket object for an airline flight """
    ticketCount = 1
    def __init__(self,event, name, date, agent, airport, destination, dep):
        super().__init__(event, name, date, agent)
        self.serialNumber = FlightTick.ticketCount
        FlightTick.ticketCount += 1
        self.airport = airport
        self.destination = destination
        self.departureTime = dep

    def __str__(self):
        return ((super().__str__()) + '\nFrom:    ' + self.airport +
                 '\nto:   ' + self.destination + '\nDeparting at: ' +
                 self.departureTime + '\nSerial Number: ' + str(self.serialNumber))        

# Global code: Create three objects for demo ---------------------------

input('\nHit "Enter" to create 1 Ticket, 1 NatsTick, and 1 FlightTick object')
t1 = Ticket('GMU Basketball', 'Ken Ball', '03/01/2024', 'GMU TicketMaster')
nt1 = NatsTick('ballgame', 'GRS', 'April 5, 2024', 'MRizzo', 'Nats Park', 'Mets')
ft1 = FlightTick('Flight', 'Anthony', 'November 27, 20230', 'ElizabethR',
                 'Washington Dulles(IAD)', 'San Francisco','7:15 pm')

print('\nObjects t1, nt1, and ft1 created \n')
