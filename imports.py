#------------------------------------------------------------------------
# IT209_A8_F20_inports.py - Functions and classes to be imported for A8.
#
# Author:  Gene Shuman         04/23/2020  
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# The 'selectMenu' function and classes that follow are provided to
# students as part of the assignment and are to be located in their own
# .py module.  

import os

def selectMenu (category, itemList):
    """itemMenu function - displays menu of variable no. of items in itemList.
       Inputs: category (Dept, etc.), list of item descriptions.
       Returns: selected menu item (integer, 1 to n), d, or x
       ---------------------------------------------------------------------"""  
    menuPic = ' '
    while menuPic != 'x':
        os.system('cls')
        print ('\n\n\t ' + category)
        print ('\n\t Select from the following items or exit ("x"): ')
        print('\n\t\t {0:3s}  {1:50s} '.format('No.', 'Description'))
        print('\t\t {0:3s}  {1:50s}'
              .format('===', '=================================================='))
        n = 0
        for i in itemList:
            print('\t\t {0:>2s} - {1:50s}  '.format(str(n+1), i.getName() ))
            n += 1
        print('\t\t {0:>2s} - {1:50s} '.format('x', 'return to previous menu '))
        menuPic = input('\n\nEnter Selection (1 to {0:>2s} or "x"): '.format(str(len(itemList))))
        if menuPic == 'x': break
        if menuPic == ' ' or menuPic == '': continue
        if int(menuPic) < 1 or int(menuPic) > len(itemList):
            input ('Invalid selection, hit "Enter" to re-select')
        else:
            name = itemList[int(menuPic) - 1].getName()
            return_object = itemList[int(menuPic) - 1]
            # input(itemList[int(menuPic) - 1].getName() + ' selected')
            break
    if menuPic == 'x' or menuPic == ' ':
        menuPic = 'x'   # Ensure caller receives an 'x' in this case
        name = None
        return_object = None
    return menuPic, name, return_object 

#------------------------------------------------------------------
# Department - Academic deparmtent class
#
# Author:  Gene Shuman      10/14/2019  (original from Spring 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Department():
    """ Department class - creates Department objects, each holding a 
        roster of student objects majoring in the Department
        ---------------------------------------------------------- """
    univ_students = 0 # class variable - total # students in all Departments
    count = 0         # class variable - total # Departments created  
    
    def __init__(self, d_code= '', d_name = '', capacity = 5, minGPA = 2.5):
        self.d_code = d_code 
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.num_students = 0
        self.avgGPA = 0.0
        self.roster = [ ]
#       self.qualified = True   # internal attribute used by addStudent()
        self.reason = ''        #    <ditto> 
        Department.count += 1
 
    def __str__(self):
        return('Department ' + self.d_code + ' ' + self.d_name + ' ' +
               ' capacity= ' + str(self.capacity) + ' number of students= ' +
               str(self.num_students) + ' min GPA= ' +
               str(self.minGPA))

    def getName(self):
        return self.d_name 
    
    def addFaculty(self, f_obj):
        if not f_obj or not isinstance(f_obj, Faculty):
            return False, 'add failed: missing or wrong obj type'
        self.roster.append(f_obj)
        return True, 'added'
        
    def addStudent(self, s_obj):
        if not s_obj or not isinstance(s_obj, Student):
            return False, 'add failed: missing or wrong obj type'
        else:
            self.qualified, self.reason = self.isQualified(s_obj)
            if self.qualified:
                self.roster.append(s_obj)
                self.num_students += 1
                Department.univ_students += 1
                self.calcAvgGPA()
                s_obj.setMajor(self.d_code)  # set Student's major to Dept
            else:
                return False, self.reason
            return True, 'added'

    def isQualified (self, s_obj):
        if self.num_students >= self.capacity:  # Check Dept. capacity
            return (False, 'add failed: over capacity')
        elif s_obj.gpa() < self.minGPA:         # Check student gpa > min
            return (False, 'add failed: minGPA')
        elif not s_obj.isEnrolled():            # Student must be enrolled 
            return (False, 'add failed: not enrolled')
        else:
            if len(self.roster) > 0:            # Check student not already
                for s in self.roster:           #   in Dept. major roster
                    if s.samePerson(s_obj):
                        return (False, 'add failed: already in Department')
        return (True, '')
        
    def calcAvgGPA(self):                       # recalculates Dept. avg GPA
        self.avgGPA = 0
        for s in self.roster:
            self.avgGPA += s.gpa()
        return (round(self.avgGPA / len(self.roster),2))

    def displayFaculty(self):
        print('\nFaculty for the ', self.d_name, ' Department: ')
        for f in self.roster:
            if isinstance(f, Faculty):
                print(f.name, ', ', f.rank)

    def listFaculty(self):   # Return list of faculty on the Dept. roster
        return [f for f in self.roster if isinstance (f, Faculty)]
         
    def printRoster(self, which = 'b', output = 'f'):
        print('\nList in Department ', self.d_name)
        for s in self.roster:
            if which == 'b':
                print(s)
            elif which == 's' and isinstance(s, Student):
                if output == 'f':
                    s.status_summary()
                else:
                    print(s)
            elif which == 'f' and isinstance(s, Faculty):
                if output == 'f':
                    s.status_summary()
                else:
                    print(s)
                
    
#------------------------------------------------------------------
# Person - Parent class for Faculty and Student classes
#
# Author:  Gene Shuman      10/14/2019  (original from Spring 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Person():
    """ Person Class - parent for Faculty and Student classes 
        ---------------------------------------- """ 
    def __init__(self, g_num, name, address, telephone, email):
        self.g_num = str(g_num) 
        self.__name = str(name)
        self.address = str(address)
        self.telephone = str(telephone)
        self.email = str(email)

    def samePerson (self, p_obj):
        return(self.g_num == str(p_obj.g_num) and
               self.getName() == str(p_obj.getName() )) # return True if g_num, name match  

    def getName(self):
        return self.__name

    def __str__(self):
        return('\n\t' + self.getName() + ', ' + str(self.g_num) +
               '\n\t  ' + self.address + ', ' + str(self.telephone) +
               '\n\t  ' + self.email)
     

#------------------------------------------------------------------
# Faculty - Faculty class, subclass of PErson
#
# Author:  Gene Shuman      10/14/2019  (original from Spring 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Faculty(Person):
    """ Faculty Class - Person subclass 
        ---------------------------------------- """ 
    def __init__(self, g_num, name, address, telephone, email, rank,
                 active, teach_load, specialty, funding):
        super().__init__(g_num, name, address, telephone, email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.funding = funding

    def __str__(self):        
        return(super().__str__() + '\n\t  ' + 'Rank: ' + str(self.rank) + '\n\t  ' +
               'Specialty: ' + str(self.specialty) + '\n')           

    def status_summary (self):
        if self.active == 'y':
            curr_status = 'active'
        else:
            curr_status = 'inactive'
        print ('\nSummary:\n\t', self.getName(), ' is a faculty member at GMU ', end = '')
        print ('with g-number ', self.g_num)
        print ('\t Their rank is ', self.rank, ' specializing in ', self.specialty)
        if self.teach_load > 0:            
            print ('\t Their teaching load is ', str(self.teach_load), end = '')
            print (' credit hours per year')

    def activate (self):
        self.active = 'y'
        return True

    def deactivate (self):
        self.active = 'n'
        return True

#------------------------------------------------------------------
# Student - Student class definition, subclass of Person
#           Identical to A3 class except it inherits from Person
#
# Author:  Gene Shuman      10/14/2019  (Original from Spring 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Student(Person):
    """ Faculty Class - creates Faculty objects, subclass of Person. 
        ------------------------------------------------------------ """ 
    def __init__(self, g_num, name, address, telephone, email,
                 status = 'Freshman', major = 'IST', enrolled = 'y',
                 credits = 0, qpoints = 0):
        super().__init__(g_num, name, address, telephone, email)
        self.status = str(status)
        self.major = str(major)
        self.enrolled = str(enrolled)
        self.credits = credits
        self.qpoints = qpoints

    def __str__(self):        
        return(super().__str__()+ '\n\t  ' + 'Major: ' + str(self.major) + '\n\t  ' +
               'Status: ' + str(self.status) + '\n\t  ' +
               'Active: ' + str(self.enrolled) + '\n\t  ' +
               'Credits: ' + str(self.credits) + '\n\t  ' +
               'GPA  = {0:4.2f}'.format(self.gpa()) + '\n') # calculate gpa, don't store           

    def gpa (self) :
        if self.credits > 0:     # prevent division by zero...
            return self.qpoints / self.credits
        else :
            return 0             # ...if zero credits, return gpa = 0

    def setMajor (self, major) :
        self.major = major
        return True
     
    def isEnrolled (self):
        return (self.enrolled == 'y')    # return True if student is enrolled

    def status_summary (self):
        if self.enrolled == 'y':
            curr_status = 'active'
        else:
            curr_status = 'inactive'
        print ('\nSummary:\n\t', self.getName(), ' is a student at GMU, ', end = '')
        print ('with g-number ', self.g_num)
        print ('\t They are a ', self.status, ' majoring in ', self.major)
        print ('\t Their gpa is {0:4.2f} and they are currently {1:8s}'
               .format(self.gpa(), curr_status) + '\n')

    def activate (self):
        self.enrolled = 'y'
        return True

    def deactivate (self):
        self.enrolled = 'n'
        return True

    
