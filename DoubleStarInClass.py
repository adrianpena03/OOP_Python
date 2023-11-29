class GrocInv(dict):
    def add(self, **kwargs):
        for item in kwargs:
            if item in self:
                self[item] += kwargs[item]
            else:
                self[item] = kwargs[item]
    
    def showInv(self):
        for item in self:
            print('\t {0:15s} - {1:3d}'.format(item, self[item]))

originalInv = {'eggs': 10, 'milk': 15, "fish": 5, 'beer': 25}

print('End of demo')

G1 = GrocInv(originalInv)

#print(G1.showInv())

# now add

G1.add(milk = 5, fish = 4, wine = 10)
print(G1.showInv())

# ------------------------
# Python Dunder Method & Syntactic Sugar 

