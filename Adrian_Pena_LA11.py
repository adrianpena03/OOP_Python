#--------------------------------------------------------------------------
#  iterators
#
#  Create the following methods for the StateIterator class to make it
#  work with the provided test script:
#
#    __next__()   - return next item in the sequence, add 1 to index
#    first()      - return first item in sequence, set index to 0
#    last()       - return last item in sequence, set index to last
#    prev()       - return previous item in sequence, subtract 1 from index
#
#  Detect the StopIteration condition for each method (see the code below).
#--------------------------------------------------------------------------
class States:

    def __init__(self, stateList):
        self.stateList = stateList

    def __iter__(self):
        return StateIterator(self.stateList)

class StateIterator:
    def __init__(self, sList):
        self.stateList = sList
        self.index = 0

    def __next__(self):
        if self.index >= len(self.stateList):
            raise StopIteration
        self.index += 1
        return self.stateList[self.index - 1]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.stateList[self.index]

    def first(self):
        if len(self.stateList) == 0:
            raise StopIteration
        self.index = 0
        return self.stateList[0]

    def last(self):
        if len(self.stateList) <= 0:
            raise StopIteration
        self.index = len(self.stateList) - 1
        return self.stateList[self.index]

    def __iter__(self):
        return self


# Global code -------------------------------------------

# Note: the states are listed in the order in which they ratified the
# U.S. constituion between 1787 and 1790.  This is the order in which
# they joined the United States.

print('\n\nT0.  Basic set-up of data and iterators.  No output.\n')
input('    Five basic tests follow.  Hit "Enter" to continue. n')
stList = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia',
          'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina',
          'New Hamshire', 'Virginia', 'New York', 'North Carolina',
          'Rhode island']

sList = States(stList)
states = iter(sList)

input('\n\nT1. Hit "Enter" to see the states list: \n')

while True:
    try:
        print (next(states))
    except StopIteration:
        print('\nEnd of list reached')
        break

input ('\n\nT2. Hit "Enter" to see the first and last item\n')
print(states.first( ) )
print(states.last ( ) )

input('\n\nT3. Hit "Enter" to see the states list in reverse order: \n')

print(states.last( ))
while True:
    try:
        print (states.prev( ))
    except StopIteration:
        print('\nEnd of reverse list reached')
        break

input('\n\nT4. Hit "Enter" to iterate the states list with a "for" loop: \n')

for s in states:
    print(s)
print('\n\nT5. Hit "Enter" to try to iterate using a "for" loop again.  There should ')
input('    not be any output since the iterator items were totally consumed.  \n')
for s in states:
    print(s)



print('\n\nEnd of Lab 11 script \n')
