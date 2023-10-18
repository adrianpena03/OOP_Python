
# while True:
#     try:
#         f = open('/Users/adrianpena/Desktop/cat.txt')
#         intext = f.read()
#         print(intext)
#         f.close()
#         a = int(input('Enter an integer: '))
#         b = int(input('Enter another integer: '))
#         print('a/b is ', a/b)
#         break
#     except FileNotFoundError:
#         print(f, 'Not found')
#     except ZeroDivisionError:
#         print('Second integer must not be zero.')

# # This code has errors
# menu = [['eggs', 3.99], ['milk', 2.50], ['pasta', 1.99], ['ale', 6.50]]
# while True:
#     try:
#         for n in range(len(menu)):
#             print(n + 1, menu[n][0], str(menu[n][1]))
#             item = int(input('Enter the item number to buy, 0 to quit: '))
#             if not item:
#                 break
#             if item < 1 or item > len(menu):
#                 raise IndexError
#         input('\nThe price of ' + menu[item -1][0] + ' is ' + str(menu[item - 1][1]))
#     except IndexError:
#         print('\n', str(item), ' not a valid menu selection.')
#     except ValueError:
#         'Type an integer in.'

# CLasses with exception class
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__('account does not have ', amount)
        self.amount = amount
        self.balance = balance

    def overage(self):
        #return self.amount - self.balance
        # or
        return self.args[1] - self.args[0]

try:
    print('\n1. Message from global code before raising exception.')
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as IWE:
    print('\nTrying to withdrawal ', IWE.overage(), ' from account')
    print('Args parameter tuple: ', IWE.args())
print('Global execution handled.')
