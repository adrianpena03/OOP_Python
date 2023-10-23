#--------------------------------------------------------------------------------------
# IT209_LA8_F23_Exceptions_template.py
#
# Lab8 template/starting kit.
#
# 1.  Create two custom exception classes: CartError and ItemError
# 2.  CartError has no logic, but the exception message will be handled by the 
#     application code (testscript) and its exception handler
# 3.  ItemError will accept a set of parameters as tuple 'self.args' and will 
#     iterate through the tuple and print each of its elements
# 4.  Complete the 'Shopping' class's add_item and remove_item methods to ensure
#     correct exception handling.  See the in-line docstring comments for hints.
# 5.  The global code that follows the 'Shopping' class runs test scenarions.
#     Embedded prints/comments explain the expected results.
#
# Review the global code to see the type of input the Shopping class methods expects.
#
# Gene Shuman     10/18/2023 (previous versions 04/04/2023, 10/25/2022)
#--------------------------------------------------------------------------------------

# 1 - 3. Add your two custom exceptions here.  Both are subclasses of
#          "Exception".
#          CartError should be two lines (signature line and 'pass')
#          ItemError (~4-5 lines) - prints the items in the self.args tuple
#            - requires the creation of a displayErrors() method that
#              iterates through the 'self.args' tuple and displays each item
class CartError(Exception):
    pass

class ItemError(Exception):
    def displayErrors(self):
        for item in self.args:
            print(item)

#---------------------------------------------------------------------------

        
class Shopping:
    allowed_items = ['Pen', 'Books', 'Coat', 'crayon', 'umbrella']
    def __init__(self,name, capacity = 5):
        self.name=name
        self.capacity = capacity
        self.inventory = [ ]
        if capacity > 5:
            raise CartError("Cart capacity must be defined as less than or equal to ", 5)
        
    def add_item(self, itemList):
        """Input: list of items (strings) to be added to the cart (self.inventory)
        Adds each item to self.inventory by appending it
        Raises: CartError if len(self.inventory) >= self.capacity, provides an appropriate
                        error message
                ItemError if an item in itemList is not in allowed_items, provides an
                        appropriate error message
     """
        for item in itemList:
            if len(self.inventory) >= self.capacity:
                raise CartError('Inventory at capacity.')
            if item not in self.allowed_items:
                raise ItemError('Not allowed in list.')
            self.inventory.append(item)

        #-------------------------------------------------------
             
    def remove_item(self,item):
        """Input: item (string) to be removed
           Removes the item from the cart (self.inventory)
           Raises: CartError if item is not in the cart (self.inventory) - provides
                   an apprporiate error message.
        """
        if item not in self.inventory:
            raise CartError(f"'{item}' not found in the cart.")
        self.inventory.remove(item)

        #--------------------------------------------------------


    def display_items(self):
        """Input:  None/self/void
           Displays the items in the cart (self.inventory)
           Raises CartError with message stating the art is empty.
        """
        # Code is provided with the template - no extra code is needed for this method
        print('\nList of items in ', self.name, ':')
        if len(self.inventory) == 0:
            raise CartError('Cart ' + self.name + ' is empty')
        else:
            for item in self.inventory:
                print(item)
           

# global code / testscript - no changes are needed to this code, just run it
#--------------------------------------------------------------------------------
print('\n\nTest 1.  Hit "Enter" to see Cart1 processed (no errors)')
input('--------------------------------------------------------------')

try:
    p1 = Shopping("Cart1")
    p1.add_item(["Pen","Books"])
    print('Pen, Books added to Cart1')
    p1.display_items()
    p1.remove_item('Pen')
    print('\nPen was removed ')
    p1.display_items()
except Exception as error:  # Generic exception handler - works here
    for m in error.args:
        print (m, end = ' ')            

print('\n\n\n\nTest 2.  Hit "Enter" to see Cart2 processed (over capacity)')
input('--------------------------------------------------------------')
try:
    p2 = Shopping("Cart2",7)
    print('Tried to create Cart2 with capacity of 7, but max is 5 ')
except CartError as error: # Handler must provide message processing for CartError
    print('\nCartError exception2: ', end = '')
    for m in error.args:
        print (m, end = ' ')

print('\n\n\n\nTest 3.  Hit "Enter" to see Cart3 processed (item not allowed)')
input('--------------------------------------------------------------')
try:
    p3 = Shopping("Cart3", 4)
    p3.add_item(["Pen","Coat","ball"])
    print('Trying to add Pen, Coat, and ball to Cart3 - ball not on allowed list')
except ItemError as error: # ItemError does message handling in its displayErrors method
    error.displayErrors()   
finally:
    p3.display_items()

print('\n\n\nTest 4.  Hit "Enter" to see Cart4 processed (item not allowed)')
input('--------------------------------------------------------------')
try:
    p4 = Shopping("Cart4", 3)
    p4.add_item(["Pen", "Coat"])
    print('Pen, Coat added to Cart4')
    p4.display_items()
    print('\nTrying to remove hat from Cart4 - hat is not in Cart4 and not an allowable item ')
    p4.remove_item('hat')     
except ItemError as error:
    error.displayErrors()
except CartError as error:
    print('\nCartError exception4: ', end = '')
    for m in error.args:
        print (m, end = ' ')
finally:
    p4.display_items()

print('\n\n\nTest 5.  Hit "Enter" to see Cart5 processed (removed item not in cart)')
input('--------------------------------------------------------------')
try:
    p5 = Shopping("Cart5", 3)
    p5.add_item(["Pen", "Coat"])
    print('Pen, Coat added to Cart5')
    print('\nTrying to remove umbrella from Cart5 - umbrella is not in Cart5 ')
    p5.remove_item('umbrella')     
except ItemError as error:
    error.displayErrors()
except CartError as error:
    print('\nCartError exception5: ', end = '')
    for m in error.args:
        print (m, end = ' ')
finally:
    p5.display_items()

print('\n\n\nTest 6.  Hit "Enter" to see Cart6 processed (already at capacity)')
input('--------------------------------------------------------------')

try:
    p6 = Shopping("Cart6", 2)
    p6.add_item(["Pen", "Coat"])
    print('Pen, Coat added to Cart5')
    p6.display_items()
    print('\nTrying to add crayon to Cart5, but already at capacity of 2')
    p6.add_item(['crayon'])     
except CartError as error:
    print('\nCartError exception6: ', end = '')
    for m in error.args:
        print (m, end = ' ')    
finally:
    p6.display_items()

print('\n\n\ntest 7.  Hit "Enter" to see Cart7 processed (cart is empty)')
input('--------------------------------------------------------------')
try:
    p7 = Shopping("Cart7", 4)
    print('Trying to display Cart7, which is empty')
    p7.display_items()
except Exception as error:
    print('\nCartError exception7: ', end = '')
    for m in error.args:
        print (m, end = ' ')    

