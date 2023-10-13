presidents = [[1789, 'Washington', 'None', 'Virginia'],
              [1797, 'Adams', 'Federalist', 'Massachusetts'],
              [1801, 'Jefferson', 'Democratic-Republican', 'Virginia'],
              [1809, 'Madison', 'Democratic-Republican', 'Virginia'],
              [1817, 'Monroe', 'Democratic-Republican', 'Virginia'],
              [1825, 'Quincy Adams', 'Democratic-Republican', 'Massachusetts'],
              [1829, 'Jackson', 'Democrat', 'Tennessee'],
              [1837, 'Van Buren', 'Democrat', 'New York'],
              [1841, 'Harrison', 'Whig', 'Virginia'],
              [1841, 'Tyler', 'Whig', 'Virginia'],
              [1845, 'Polk', 'Democrat', 'Tennessee'],
              [1849, 'Taylor', 'Whig', 'Kentucky'],
              [1853, 'Pierce', 'Democrat', 'New Hampshire'],
              [1857, 'Buchanan', 'Democrat', 'Pennsylvania'],
              [1861, 'Lincoln', 'Republican', 'Illinois'],
              [1865, 'Lincoln', 'Republican', 'Illinois'],
              [1865, 'Johnson', 'National Union', 'Tennessee'],
              [1869, 'Grant', 'Republican', 'Ohio'],
              [1877, 'Hayes', 'Republican', 'Ohio'],
              [1881, 'Garfield', 'Republican', 'Ohio'],
              [1881, 'Arthur', 'Republican', 'Vermont'],
              [1885, 'Cleveland', 'Democrat', 'New Jersey'],
              [1889, 'Harrison', 'Republican', 'Ohio'],
              [1893, 'Cleveland', 'Republican', 'Ohio'],
              [1897, 'McKinley', 'Republican', 'Ohio'],
              [1901, 'McKinley', 'Republican', 'Ohio'],
              [1901, 'Roosevelt', 'Republican', 'New York'],
              [1909, 'Taft', 'Republican', 'Ohio'],
              [1913, 'Wilson', 'Democrat', 'Virginia'],
              [1921, 'Harding', 'Republican', 'Ohio'],
              [1925, 'Coolidge', 'Republican', 'Massachusetts'],
              [1929, 'Hoover', 'Republican', 'Iowa'],
              [1933, 'Roosevelt', 'Democrat', 'New York'],    
              [1945, 'Roosevelt', 'Democrat', 'New York'],    
              [1945, 'Truman', 'Democrat', 'Missouri'],       
              [1953, 'Eisenhower', 'Republican', 'Kansas'],
              [1961, 'Kennedy', 'Democrat', 'Massachusetts'],
              [1963, 'Kennedy', 'Democrat', 'Massachusetts'],  
              [1963, 'Johnson', 'Democrat', 'Texas'],          
              [1969, 'Nixon', 'Republican', 'California'],
              [1974, 'Nixon', 'Republican', 'California'],     
              [1974, 'Ford', 'Republican', 'Michigan'],       
              [1977, 'Carter', 'Democrat', 'Georgia'],
              [1981, 'Reagan', 'Republican', 'California'],
              [1989, 'Bush', 'Republican', 'Texas'],
              [1993, 'Clinton', 'Democrat', 'Arkansas'],
              [2001, 'Bush', 'Republican', 'Texas'],
              [2009, 'Obama', 'Democrat', 'Illinois'],
              [2017, 'Trump', 'Republican', 'New York'],
              [2021, 'Biden', 'Democrat', 'Delaware'] ]

class USPresidents(list):
    """Code that Manages and Organizes president information.
       Includes year, name, party, and state.
       
       Created by Adrian Pena."""

    def __init__(self, inlist):
        # Constructor, initializes current year and inlist
        super().__init__()
        for i in inlist:
            self.append(i)
        self.currentYear = 2023

    def whoWasPrez(self, year):
            # Gets president of given year as input
            if year < 1789 or year > self.currentYear:
                return 'out of range'
            else:
                presidents_in_year = [president[1] for president in self if president[0] <= year and (president[0] + 4) > year]
                return presidents_in_year

    def partyCount(self):
        # counts number of party members for each category
        democrats = sum(1 for i in self if i[2] == 'Democrat')
        republicans = sum(1 for i in self if i[2] == 'Republican')
        other = sum(1 for i in self if i[2] not in ['Democrat', 'Republican'])
        return democrats, republicans, other
    
    def stateList(self, state):
        # returns lists of presidents who were born in a specific state
        presidents_from_state = []
        for i in self:
            if i[3] == state:
                if i[1] not in presidents_from_state:
                    presidents_from_state.append(i[1])
        return presidents_from_state
        
# Global/executable code that tests the class and its methods
PL = USPresidents(presidents)

# Should return 63:
print('T1. Size of list (should be 50): ', len(PL), '\n')

# Should return 'Biden':
input('\nHit "Enter" to run T2. Most recent president: ')
print(PL[-1][1])

# Should return 'Lincoln':
prez = PL.whoWasPrez(1861)
input('\nHit "Enter" to run T3. President who took office in 1861: ' )
print(prez)

# Should return 'Harrison, Tyler'
prez = PL.whoWasPrez(1841)
input('\nHit "Enter" to run T4. Presidents in 1841, should be Harrison and Tyler: ')
print(prez)

# Should return 'Roosevelt and McKinley'
prez = PL.whoWasPrez(1901)
input('\nHit "Enter" to run T5. Presidents in 1901, should be McKinley and Roosevelt: ')
print(prez)

# Should return 'Roosevelt, Truman'
prez = PL.whoWasPrez(1945)
input('\nHit "Enter" to run T6. Presidents in 1945, should be Roosevelt and Truman: ')
print(prez)

# Should return 'Biden':
prez = PL.whoWasPrez(2023)
input('\nT7. President who was in office in 2023: ')
print(prez)

# Should display an 'out of range' error:
input ('\nHit ""Enter" to run T8. President who was in office in 1788: ')
print(PL.whoWasPrez(1788))

# Should display three counts, Dems, Repubs, Other:
input('\nHit "Enter" to run T9. Number of presidents in the various parties (17, 23, 10)')
result = PL.partyCount()
print ('\tT9. Democrats:   ', result[0])
print ('\tT9. Republicans: ', result[1])
print ('\tT9. Other:       ', result[2])

# Should display seven presidents from Virginia in a list:
print('\nHit "Enter" to run T10. List of presidents from Virginia (should be 7): \n')
pList = PL.stateList('Virginia')
print(pList)

print('\nEnd of Lab #7 Test')