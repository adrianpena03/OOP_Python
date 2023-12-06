#--------------------------------------------------------------------------------------
# GUI_Class
#
# Shopping, CartError and ItemError classes.(Similar to LA8, slightly modified)
#
# Created: 11/6/2023
#--------------------------------------------------------------------------------------

class CartError(Exception):
    pass

class ItemError(Exception):
    def displayErrors(self):
        error_message = '\nItemError exception: '
        for p in self.args:
            error_message += str(p)
        return error_message

class Shopping:
    available_items = ['Pen', 'Books', 'Coat', 'Crayon', 'Umbrella'] #modified
    def __init__(self,name, capacity = 5): #modified
        self.name=name
        self.capacity = capacity
        self.inventory = [ ]

    def add_item(self,item):
        if len(self.inventory) >= self.capacity:
            raise CartError("Cart is overcapacity")
        if item in Shopping.available_items: #modified
            self.inventory.append(item)
        else:
            raise ItemError("Item is not available") #modified

    def remove_item(self,item):
        if item not in self.inventory:
            raise CartError("Item is not in the cart") #modified
        self.inventory.remove(item)
