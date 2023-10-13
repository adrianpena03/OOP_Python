#------------------------------------------------------------------
# IT209_LA6_inheritance_account_F23_template.py  - Lab #6
#
# Given:  Account class
# Create: CheckingAccount as a subclass of Account
#
# CheckingAccount:
#    supplies its own 'interest' class variable with value .01
#    adds its own withdrawal_charge class variable with value 10 
#    inherits the __init__, deposit, and printStatement methods
#                 and uses them as it is (i.e. no changes)
#    overrides calcInterest by supplying its own method and doesn't
#                 use anything from the parent (uses its own
#                 interest rate).
#    overrides withdraw, but runs the parent method ('super()') 
#                 while supplying its own 'amount' parameter
#                 (= amount + withdrawal_charge) 
#
# Gene Shuman         10/04/2023 
#------------------------------------------------------------------

class Account:
    interest = 0.02
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    def __init__(self, account_holder, acctType = 'Savings'):        
        self.balance = 0.0
        self.holder = account_holder
        self.type = acctType
        interest = 0.02
        self.transactionLog = [ ]     # [date, type, amount, balance]
    def deposit (self, date, amount):
        self.balance += amount
        self.transactionLog.append([date, 'deposit', amount, self.balance])
        return self.balance
    def calcInterest(self):
        self.monthlyInterest = self.balance * Account.interest
        self.balance = self.balance + self.monthlyInterest
        return self.monthlyInterest, self.balance 
    def withdraw (self, date, amount):
        if amount > self.balance:
            return 'Insufficient Funds'
        self.balance -= amount
        self.transactionLog.append([date, 'withdrawal', amount, self.balance])
        return self.balance
    def printStatement (self, month = 10):
        print ('\nStatement for ', Account.months[month - 1], ' --------------------')
        print ('Account holder: ', self.holder, '   Type: ', self.type, '\n')
        print('{0:6s} {1:11s}   {2:8s}   {3:8s}'.format('Date', 'Transaction', 'Amount', 'Balance'))
        print('{0:6s} {1:11s}   {2:8s}   {3:8s}'.format('======', '===========', '========', '=========')) 
        for t in self.transactionLog:
            print('{0:6s} {1:10s}   ${2:8.2f}   ${3:8.2f}'.format(t[0], t[1], t[2], t[3]))     
        a, b = self.calcInterest()
        print('{0:6s} {1:10s}   @{2:5.2f}      ${3:8.2f}'.format('10/30', 'Interest', self.interest, a))  
        print('\n{0:6s} Ending balance           ${1:8.2f}'.format(str(month) + '/30', b))
        print('-------------------------------------------------')

#Add sublcass code here: ------------------------------------------------
class CheckingAccount(Account):
    # Sub-class of class Account that overrides methods from parent class, and overrides some values.
    # Contains methods to calculate a Checking Account interest, and a Withdraw method

    # Created by Adrian Pena
    interest = 0.01
    withdrawal_charge = 10
    def __init__(self, account_holder, acctType='Checking'):
        super().__init__(account_holder, acctType)

    def calcInterest(self):
        # Override calcInterest with the interest rate for CheckingAccount
        self.monthlyInterest = self.balance * CheckingAccount.interest
        self.balance = self.balance + self.monthlyInterest
        return self.monthlyInterest, self.balance

    def withdraw(self, date, amount):
        # Override withdraw to include the withdrawal charge
        total_withdrawal = amount + CheckingAccount.withdrawal_charge
        if total_withdrawal > self.balance:
            return 'Insufficient Funds'
        self.balance -= total_withdrawal
        self.transactionLog.append([date, 'withdrawal', total_withdrawal, self.balance])
        return self.balance
    

#   Global/Executable test code follows ------------------------------------
input('\n\nHit "Enter" to set up a Saving Account --------------------\n')
a1 = Account('Jeff')
a1.deposit('10/04', 1000)
print('\nObject a1, account holder and balance = ', a1.holder, a1.balance)
# Expected output: the first withdrawal attempt should fail, the second should succeed
input('\nHit "Enter" to withdraw from this account ')
print ('withdrawing $1100 from: ', a1.holder, ', result: ', a1.withdraw('10/05', 1100))
print ('withdrawing $100 from ', a1.holder, ' account, balance: ', a1.withdraw('10/05', 100))


input('\n\nHit "Enter" to set up a Checking Account ----------------\n')
c1 = CheckingAccount('Elizabeth', acctType = 'Checking')
c1.deposit('10/04', 2000)
print('\nObject c1, account holder and balance = ', c1.holder, c1.balance)
# Expected output: the first withdrawal attempt should fail, the second should succeed
#                  A withdrawal charge should be applied
input('\nHit "Enter" to withdraw from this account ')
print('withdrawing $2100 from: ', c1.holder, ', result: ', c1.withdraw('10/05', 2100))
print('withdrawing $100 from ', c1.holder, ' checking, balance: ', c1.withdraw('10/05', 100))

input('\n\nHit "Enter" to see monthly statements ---------------------\n')
# Expected output: accounts will show different interest rates, checking will show
#                  a withdrawal charge applied
# Both account class types use the same inherited 'printstatement()' method
a1.printStatement(10)
c1.printStatement(10)
