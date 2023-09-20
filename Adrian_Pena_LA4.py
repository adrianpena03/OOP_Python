class Baggage:
    allowed_items = ("pen", "book", "coat")
    def __init__(self, name, capacity=5):
        """This code manages items in an inventory of class Baggage, 
        such as displaying, adding, removing, and checking if items are in the inventory
        
        Created by Adrian Pena. """
        self.name = name
        self.capacity = capacity
        self.inventory = []

    def display_items(self):
        # Displays items inventory
        return f'Inventory: {self.inventory}, Name: {self.name}, Capacity: {self.capacity}'
            
    def add_item(self, o_obj):
        # Adds item to inventory list
        if len(self.inventory) < self.capacity:
            if o_obj.name in self.allowed_items:
                self.inventory.append(o_obj.name)
                return True, f"{o_obj.name} added."
            return False, "Invalid item."
        else:
            return False, "At capacity."

    def remove_item(self, o_obj):
        # Removes an item from inventory list, but first checks to see if it is there
        if self.check_item(o_obj):
            return True, o_obj + " removed."
        return False, "Item not in baggage."

    def check_item(self, o_obj):
        # Checks if an objet is in inventory list
        return o_obj.item_name in self.inventory


class InvItem:
    def __init__(self, name, item_name = ""):
        self.name = name
        self.item_name = item_name


# Global Executable code follows......................................
        
input('Hit "Enter" to create "backpack1" object with name "My backpack1": \n')
backpack = Baggage('My backpack1')
backpack.display_items()

input('Hit "Enter" to create some "InvItem" objects: \n')
It1 = InvItem("book")
It2 = InvItem("umbrella")
It3 = InvItem("coat")
It4 = InvItem("pen")
It5 = InvItem("cap")
It7 = InvItem("banana")
print('Created: ', It1.name, It2.name, It3.name, It4.name, It5.name, It7.name) 

print('\nT1. Hit "Enter" to add \n\t', It1.name, '\n\t', It2.name,
      '\n\t', It4.name, '\nto ', backpack.name, '\n')
backpack.add_item(It1)
backpack.add_item(It2)
backpack.add_item(It4)
backpack.add_item(It7)
backpack.display_items()

input('\nT2. "Enter" to see if ' + backpack.name + ' has ' + It1.name)
print(backpack.check_item(It1))
input('\nT3. "Enter" to see if ' + backpack.name + ' has ' + It7.name)
print(backpack.remove_item(It7))
input('\nT4. "Enter" to remove ' + It1.name + ', result: ' + backpack.remove_item(It1)[1])
input('\nT5. "Enter" to add ' + It3.name + ',  result: ' + backpack.add_item(It3)[1])
print('\nShould now have umbrella, pen, and coat...')
backpack.display_items()

input('\nT6. Creating new container with name "My satchel" - add 2 items to container equal capacity ')
satchel = Baggage('My satchel', capacity=2)
satchel.add_item(It3)
satchel.add_item(It4)
print('\n', satchel.name, ' was created with the following items: ')
satchel.display_items()
input('\nT7. "Enter" to try to add a third item ' + It5.name + ' to force over-capacity condition ')
result, message = satchel.add_item(It5)
print (result, message)

print('\n\nEnd of Lab#4 test script')