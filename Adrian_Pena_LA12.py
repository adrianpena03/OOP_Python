#--------------------------------------------------------------------------------------
#  IT209_LA12_F23_GUI_template  (GRS uodates)
#
#  Review the GUI screen specification and line placement in the A9 spec document.
#  Provide code for widgets #3-9 and the remove() method.
#
#  Instructions:
#
#  (1) Review the LA12 specification document and GUI screen.  Determine how many
#      grid lines will be required to display what's needed on the screen: ~13 will
#      work.
#  (2) The widgets needed are (you provide code for widgets 3-9 below):
#       1. Label widget for 'Welcome' message (given)
#       2. Label widget for 'Items Avalable' message (given)
#       3. Label widget for item name (you provide code)
#       4. StringVar to hold name of item selected (you provide)
#       5. Entry widget to collect typed item name input (you provide)
#       6. Button widget 'Add item' - adds selected item to cart object when pushed (you provide)
#       7. Button widget 'Remove item' - removes selected item when pushed (you provide)
#       8. Label widget for status message to show added, removed, or error message (you provide)
#       9. Label widget to hold items in cart (you provide)
#  (3) Provide code for the remove() method 
#      10. remove() method code to remove item from cart (you provide)

#---------------------------------------------------------------------------------------


from tkinter import *
from IT209_LA12_F23_GUI_Class import CartError, ItemError, Shopping

class ShoppingFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self,root)
        self.data = StringVar(self, '')
        self.create_components()
        self.item_list = []


    def create_components(self):
        # 1. Label: create and grid layout 'Welcome' message 
        self.title_label = Label(self, text = 'Welcome to Mason Bookstore')
        self.title_label.grid(row=2, column = 1)

        # 2. Label: Create and grid layout 'Items Available...' 
        self.available_label = Label(self, text = 'Items Available: Pen, Books, Coat, Crayon, Umbrella')
        self.available_label.grid(row=3, column = 1)

        #-------------------------------------------------------------------------------
        # For Lab #12 - add code for widgets 3 - 9 below, and for the remove() method
        #-------------------------------------------------------------------------------

        # 3. Label: create and grid layout label for item name
        self.item_name_label = Label(self, text='Item Name:')
        self.item_name_label.grid(row=4, column=0)

        # 4. StringVar: TextVariable - create StringVar to hold item name
        self.contents = StringVar()

        # 5. Entry: create and grid layout entry for item
        self.item_entry = Entry(self, textvariable=self.contents)
        self.item_entry.grid(row=4, column=1)

        # 6. Button: Add Item - create and grid layout ... (2 lines of code)
        #     ....create button command that need to be set with add() method
        self.add_button = Button(self, text='Add Item', command=self.add)
        self.add_button.grid(row=4, column=2)

        # 7. Button: Remove Item - create and grid layout ... (2 lines of code)
        #     ....create button command that need to be set with remove() method
        self.remove_button = Button(self, text='Remove Item', command=self.remove)
        self.remove_button.grid(row=4, column=3)

        # 8. Label status message - create and grid layout
        self.status_label = Label(self, textvariable=self.data)
        self.status_label.grid(row=5, column=1)

        # 9. Label: create and layout a label for cart items display
        self.cart_label = Label(self, text="Cart:", foreground='blue')
        self.cart_label.grid(row=6, column=0, columnspan=4)


    def add(self):
        # item_name is defined as a StringVar and is fetched using get()
        item = self.contents.get()

        # item will be added to the cart using add_item() method from Shopping class
        # Item will be added to the item_list and will be displayed in the cart label
        # Added Successfully message will be displayed
        # Raises: Cart Error if the cart is overcapacity
        # Raises: Item Error if the item is not available and use displayErrors() method from ItemError class
        try:
            shopping_cart.add_item(item)
            self.item_list.append(item)

            cart_items = "\n".join(self.item_list)
            self.cart_label.config(text="Cart:\n" + cart_items)
            self.data.set("Added Successfully")  # Set the status for displaying on the screen

        except CartError as e:
            self.data.set(str(e))

        except ItemError as i:
            error_message = i.displayErrors()
            self.data.set(error_message)  # Set the error message for displaying on the screen


    # 10. Create the code for the remove function using the shopping cart 'remove()' method.
    #         Similar to the add() method above - should be ~8-10 lines of code.
    def remove(self):
        # get item name from the entry widget
        item = self.contents.get()

        # Use try-except block.
        try:
            shopping_cart.remove_item(item)
            # Remove item from the item_list
            self.item_list.remove(item)

            cart_items = "\n".join(self.item_list)
            self.cart_label.config(text="Cart:\n" + cart_items)
            self.data.set("Removed Successfully")

        except CartError as e:
            # Raises: Cart Error if the item is not in the cart
            self.data.set(str(e))

        except ItemError as i:
            # Handle ItemError and set the error message for displaying on the screen
            error_message = i.displayErrors()
            self.data.set(error_message)


shopping_cart=Shopping("Shopping Cart", 5) # shopping instance created
root = Tk()
root.geometry("400x400") # Size
f = ShoppingFrame(root)    # GUI window created as a Frame object inside the root object
f.grid()
root.mainloop()
