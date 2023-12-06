#----------------------------------------------------------------------------
# IT209_A6_F23_test_script.py -Person/Student/Faculy class
#                  Inheritance hierarchy
#
# Shows the use of polymorphism - executing different object types
# with the same code.
#
#----------------------------------------------------------------------------

"""A6 Created by Adrian Pena"""

class Person:
    currentYear = 2023
    personCount = 10

    def __init__(self, name, address, telephone, email):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        self.g_num = 'G' + '0' * (6 - len(str(Person.personCount))) + str(Person.personCount)
        Person.personCount += 1

    def __str__(self):
        # displays attributes in string
        return 'Person: ' + self.g_num + ' ' + self.name + ' ' + self.address

    def dupePerson(self, p_obj):
        #  returns True or False depending on if g number, an object and name are same
        return self.g_num == p_obj.g_num and self.name == p_obj.name


class Student(Person):
    totalEnrollment = 0

    def __init__(self, name, address, telephone, email, major='IST', enrolled='y', credit=0, qpoints=0):
        super().__init__(name, address, telephone, email)  # Call the parent class constructor
        self.major = major
        self.enrolled = enrolled
        self.credit = credit
        self.qpoints = qpoints
        Student.totalEnrollment += 1
        self.g_num = f'G{Student.totalEnrollment:05}'

    def __str__(self):
        # string method which uses inheritance of Person class
        return 'Student: ' + super().__str__() + ' ' + self.major

    def gpa(self):
        # Calculates GPA
        if self.credit == 0:
            return 0.0
        return self.qpoints / self.credit

    def addGrade(self, grade, credits):
        # Calculates GPA points for student, returns True if the grade was added successfully, False otherwise
        grade_values = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
        if grade in grade_values and 0 <= credits <= 4:
            qpoints = grade_values[grade] * credits
            self.credit += credits
            self.qpoints += qpoints
            return True
        else:
            return False

    def isActive(self):
        # Checks if a student is enrolled. Returns "Y" if enrolled and "N" if not
        if self.enrolled.lower() == "y":
            return "Y"
        else:
            return "N"

    def classLevel(self):
        # Calculates class level based on credits completed
        if self.credit >= 90:
            return 'Senior'
        elif self.credit >= 60:
            return 'Junior'
        elif self.credit >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def setMajor(self, newMajor):
        # set method for self.major
        self.major = newMajor

    def case_summary(self):
        # creates a summary for a student's information
        return (
        f"{self.name} is a student at GMU, with g-number {self.g_num}\n"
        f"They are a {self.classLevel()} majoring in {self.major}\n"
        f"Their gpa is {self.gpa()} and they are currently {self.enrolled}"
        )

    def activate(self):
        # acttvates the student
        self.enrolled = 'enrolled'
        return True

    def deactivate(self):
        # deactivate the student
        self.enrolled = 'not enrolled'
        return True

    def getStatus(self):
        # check if a student is currently enrolled
        if self.enrolled.lower() == "y":
            return "enrolled"
        else:
            return "not currently enrolled"


class Faculty(Person):

    def __init__(self, name, address, telephone, email, rank, active, teach_load, specialty, yearStarted):
        super().__init__(name, address, telephone, email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.yearStarted = yearStarted

    def __str__(self):
        # string method
        return 'Faculty: ' + super().__str__() + ' ' + self.rank + ' ' + self.specialty + ' ' + str(self.tenure())

    def tenure(self):
        # returns years of tenure for a faculty member
        return Person.currentYear - self.yearStarted
    
    def case_summary(self):
        # Creates summary of faculty member info
        return (
            f"{self.name} is a faculty member at GMU with g-number {self.g_num}\n"
            f"Their rank is {self.rank} specializing in {self.specialty}\n"
            f"Their teaching load is {self.teach_load} credit hours per year"
        )

    def activate(self):
        # Activate faculty member
        self.active = 'active'
        return True

    def deactivate(self):
        # Deactive faculty member
        self.active = 'not active'
        return True

    def getStatus(self):
        # check if the faculty member is currently active
        if self.active.lower() == "y":
            return "active"
        else:
            return "not active"

class Department:
    univ_students = 0
    count = 0

    def __init__(self, d_code='', d_name='', capacity=25, minGPA=3.00):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.avgGPA = 0.0
        self.roster = []

    def __str__(self):
        # string method
        return (
            'Department: ' + self.d_name + ' (' + self.d_code + ') ' +
            'Capacity: ' + str(self.capacity) +
            ' Students: ' + str(len(self.roster))
        )

    def addStudent(self, student_obj):
        # adds student to department roster. Returns True if added successfully, False and reason message otherwise
        if not student_obj or not isinstance(student_obj, Student):
            return False, 'add failed: missing or wrong object type'
        if len(self.roster) >= self.capacity:
            return False, 'add failed: over capacity'
        qualified, reason = self.isQualified(student_obj)
        if qualified:
            self.roster.append(student_obj)
            Department.univ_students += 1
            self.calcAvgGPA()
            student_obj.setMajor(self.d_code)
            return True, 'added'
        return False, reason
    
    def addFaculty(self, faculty_obj):
        # adds a faculty member to the department roster
        if not faculty_obj or not isinstance(faculty_obj, Faculty):
            return False, 'add failed: missing or wrong object type'
        self.roster.append(faculty_obj)
        return True, 'added'

    def isQualified(self, student_obj):
        # Check if a student is qualified to be added to the department
        if student_obj.gpa() < self.minGPA:
            return False, 'Could not add student: GPA must be 3.00 minimum.'
        for s in self.roster:
            if s.dupePerson(student_obj):
                return False, 'Could not add student: Student already enrolled.'
        if not student_obj.isActive():
            return False, 'Could not add student: Not enrolled in the university.'
        return True, 'Added student.'

    def showRoster(self, filter='b'):
        # Display case summary for students, faculty, or both 'b', in the department
        for person in self.roster:
            if filter == 's' and isinstance(person, Student):
                print(person.case_summary())
            elif filter == 'f' and isinstance(person, Faculty):
                print(person.case_summary())
            elif filter == 'b':
                print(person.case_summary())

    def calcAvgGPA(self):
        # calculates average GPA of students in the department.
        total_gpa = 0.0
        num_students = 0
        for person in self.roster:
            if isinstance(person, Student):
                total_gpa += person.gpa()
                num_students += 1
        if num_students > 0:
            self.avgGPA = round(total_gpa / num_students, 2)
        else:
            self.avgGPA = 0.0
        return self.avgGPA

# Global Code starts here ---------------------------------------------------        

print('\nStart of A6 test script *****************************\n')
print('\nTest 1.  Creating 6 Student objects, 3 Faculty objects, ')
print(' and one Department object - Engineering - for use in this testscript.')
print('---------------------------------------------------------------------------')
s1 = Student('David Miller', '321 Maple Lane, Vienna, VA',
      '571-285-4567', 'dmiller8@gmu.edu',major = 'Hist', enrolled = 'y',
      credit = 30, qpoints = 90)           
s2 = Student('Bonnie Bonilla', '123 Oak Street, Potomac, MD',
      '301-285-4567', 'bbonilla@gmu.edu',major = 'Math',enrolled = 'y',
      credit = 90, qpoints = 315)
s3 = Student('Chris Squire', '4567 Park Lane, London, UK',
      '425-285-4567', 'csquire8@gmu.edu', major = 'Musc', enrolled = 'y',
      credit = 45, qpoints = 160)
s4 = Student('Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov', major = 'Musc', enrolled = 'y',
      credit = 75, qpoints = 250)    
s5 = Student('Geddy Lee', '1240 Pacific Road, Loa Angeles, CA',
      '231-44-2596', 'grahamcentralsta@gmail.com', major = 'CHHS', enrolled = 'y',
      credit = 105, qpoints = 320)           
s6 = Student('John Entwistle', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', major = 'CSci', enrolled = 'y',
      credit = 15, qpoints = 35)
     
f1 = Faculty('Amanda Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'ashuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)  
f2 = Faculty('A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)

d1 = Department('ENGR', 'Engineering', 5, 3.0)
d1.addFaculty(Faculty('Alan Turing', '6 Stable Way, Bletchly Park, U.K.',
             '9-56-4955', 'aturing@UK.gov', 'Associate Professor', 'y',
             6, 'research', 1943))

d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)
d1.addStudent(s4)
d1.addFaculty(f1)
d1.addFaculty(f2)
d1.addStudent(s4)  
d1.addStudent(s5)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(f1)
print(f2)
print('Faculty #3 is Alan Turing')
print(d1)

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 2.  Hit "Enter" to see Engineering Dept. Student case summaries - 5 students: ')
print('----------------------------------------------------------------------------------\n')
d1.showRoster('s')

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 3.  Hit "Enter" to see Engineering Dept. All case summaries - 5 students and 3 faculty: ')
print('------------------------------------------------------------------------------\n')
d1.showRoster('b')

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 4.  Hit "Enter" to deactivate  '+ s1.name + ' and ' + f2.name)
print('---------------------------------------------------------------------------\n')
print(s1.name, ' current status is ', s1.getStatus())
print(f2.name, ' current status is ', f2.getStatus())
print(s1.name, ' deactivation result: ', s1.deactivate())
print(f2.name, ' deactivation result: ', f2.deactivate())
print(s1.name, ' updated status is ', s1.getStatus())
print(f2.name, ' updated status is ', f2.getStatus())

#--------------------------------------------------------------------------------------------
input('\n\n\nTest 5.  Hit "Enter" to activate  ' + s1.name)
print('---------------------------------------------------------------------------\n')
print(s1.name, ' activation result: ', s1.activate())

print('\n\n\n***** End of A6 test **********')
