class Department():

    """This class manages university department student rosters based on specific 
    qualifications and tracking department related information.
    
    Created by Adrian Pena"""

    univ_students = 0
    count = 0 
    
    def __init__(self, d_code= '', d_name = '', capacity = 25, minGPA = 3.00):
        # Initialize values
        self.d_code = d_code 
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.avgGPA = 0.0
        self.studentRoster = []
        Department.count = Department.count + 1
 
    def __str__(self):
        # Method that returns class attributes as a string
        return(
               'Department: ' + self.d_name + ' (' + self.d_code + ') ' +
               'Capacity: ' + str(self.capacity) + 
               'Student Roster: ' + str(len(self.studentRoster))
               ) 
    
    def addStudent(self, student_obj):
        # Adds student to roster using isQualified method
        if not student_obj or not isinstance(student_obj, Student):
            return False, 'add failed: missing or wrong object type'

        if len(self.studentRoster) >= self.capacity:
            return False, 'add failed: over capacity'

        qualified, reason = self.isQualified(student_obj)

        if qualified:
            self.studentRoster.append(student_obj)
            Department.univ_students += 1
            self.calcAvgGPA()
            student_obj.setMajor(self.d_code)
            return True, 'added'
        
        return False, reason


    def isQualified(self, student_obj):
        # Determines if student is qualified to enroll in department
        if student_obj.gpa() < self.minGPA:
            return False, 'Could not add student: GPA must be 3.00 minimum.'
        
        if not student_obj.isActive():
            return False, 'Could not add student: Not enrolled in university.'
        
        if any(s.eqStudent(student_obj) for s in self.studentRoster):
            return False, 'Could not add student: Student already enrolled.'
        
        return True, 'Added student.'

    def showStudents(self):
        # Displays students in student roster
        for i in self.studentRoster:
            print(i)

    def calcAvgGPA(self):
        # Calculates average GPA among students in roster
        total_gpa = sum(student.gpa() for student in self.studentRoster)
        num_students = len(self.studentRoster)

        if num_students > 0:
            self.avgGPA = round(total_gpa / num_students, 2)
        else:
            self.avgGPA = 0.0

        return self.avgGPA


# ------------------------------------------------------------
class Student:
    totalEnrollment = 0
    g_num_counter = 0

# This code manages student information by calculating gpa, adding grades, student enrollment, 
# class level, and comparing student objects.

# Created by Adrian Pena

    def __init__(self, name, major='IST', enrolled='y', credit=0, qpoints=0):
        self.name = name
        self.major = major
        self.enrolled = enrolled
        self.credit = credit
        self.qpoints = qpoints

        Student.totalEnrollment += 1
        self.g_num = f'G{Student.totalEnrollment:05}'

    def __str__(self):
        # Returns attributes as a string
        return (
            "Name: " + str(self.name) +
            ", Major: " + self.major +
            ", Enrolled: " + str(self.enrolled) +
            ", Credit: " + str(self.credit) +
            ", QPoints: " + str(self.qpoints)
        )

    def gpa(self):
        # Calculates the GPA by dividing quality points over credits
        if self.credit == 0:
            return 0.0
        return self.qpoints / self.credit

    def addGrade(self, grade, credits):
        # Adds grade to dictionary depending on credits and q points
        grade_values = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
        if grade in grade_values and 0 <= credits <= 4:
            qpoints = grade_values[grade] * credits

            self.credit += credits
            self.qpoints += qpoints
            return True
        else:
            return False

    def isActive(self):
        # Determines whether a student is enrolled or not
        if self.enrolled.lower() == "y":
            return True
        elif self.enrolled.lower() == "n":
            return False

    def classLevel(self):
        # Determines student class level based on # of credits completed
        if self.credit >= 90:
            return 'Senior'
        elif self.credit >= 60:
            return 'Junior'
        elif self.credit >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def eqStudent(self, other_student):
        # compares student object to gnum to see if they are the same
        if self.g_num == other_student.g_num and self.name == other_student.name:
            return True
        else:
            return False

    def setMajor (self, NewMajor):
        # Setter method for new major
        self.major = NewMajor
        return True
        
                
# Global/executable code ---------------------------------------------------

print('\nStart of Department and Student class demo **************')
input('\nTest1. Hit "Enter" to create 16 student objects for use in the demo ')
s1 = Student('David Miller', major = 'Hist',
      enrolled = 'y', credit = 30, qpoints = 90)           
s2 = Student('Sonia Fillmore', major = 'Math',
      enrolled = 'y', credit = 90, qpoints = 315)
s3 = Student('Chris Squire', major = 'Musc',
      enrolled = 'y', credit = 45, qpoints = 160)           
s4 = Student('Tal Wilkenfeld', major = 'ARTS',
      enrolled = 'y', credit = 70, qpoints = 225)
s5 = Student('Larry Graham', major = 'CHHS',
      enrolled = 'y', credit = 105, qpoints = 315)           
s6 = Student('Dave Holland', major = 'CSci',
      enrolled = 'y', credit = 15, qpoints = 39)
s7 = Student('Esperanza Spalding', major = 'ENGR',
      enrolled = 'y', credit = 65, qpoints = 250)           
s8 = Student('Tim Bogert', major = 'Hist',
      enrolled = 'y', credit = 45, qpoints = 126)
s9 = Student('Gordon Sumner', major = 'Musc',
      enrolled = 'y', credit = 15, qpoints = 45)           
s10 = Student('Paul McCartney', major = 'ARTS',
      enrolled = 'y', credit = 110, qpoints = 330)
s11 = Student('Tina Weymouth', major = 'ENGR',
      enrolled = 'y', credit = 85, qpoints = 250)
s12 = Student('John McVie', major = 'Hist',
      enrolled = 'y', credit = 45, qpoints = 126)
s13 = Student('Nawt enrolled', major = 'Hist',
      enrolled = 'n', credit = 45, qpoints = 120)
s14 = Student('Toolow G. Peyay', major = 'Undc',
      enrolled = 'y', credit = 20, qpoints = 38)
s15 = Student('Stanley Clark', major = 'Chem',
      enrolled = 'y', credit = 95, qpoints = 295)
s16 = Student('Geddy Lee', major = 'Chem',
      enrolled = 'y', credit = 58, qpoints = 143)

print('\nList of Students created-------------------------------:\n ')
print('s1=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)      
print('s5=  ',s5)
print('s6=  ',s6)      
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)      
print('s13= ',s13)
print('s14= ',s14)
print('s15= ', s15)
print('s16= ', s16)
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 5, 2.5)
d3 = Department('CHHS', 'College of Health and Human Services', 3, 2.75)

input('\n\nTest2. Hit "Enter" to see the list of 3 Department objects created ')
print('\n\nDepartments established---------------------------------:')
print(d1)
print(d2)
print(d3)

input('\n\n\nTest3. Hit "Enter" to add s1 - s5 to ENGR Department- print student list\n')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)      
d1.addStudent(s4)
d1.addStudent(s5)
d1.showStudents()      


input('\n\n\n\nTest4. Hit "Enter" to add additional students to various departments -------------------:')
a, b = d1.addStudent(s15)
print('\nAttempting to add ', s15.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nDepartment ', d1.d_name, ' student list is now: ')
d1.showStudents()
      
input('\n\n\n\nTest5. Hit "Enter" to add two students to the ARTS Department ')
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s6)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s7)
print('\t\t\treturn values: ', a, '  reason code: ', b)
d2.showStudents()

input('\n\n\n\nTest6. Hit "Enter" to add two students to the CHHS Department' )
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s8)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s9)
print('\t\t\treturn values: ', a, '  reason code: ', b)
d3.showStudents()

input('\n\n\n\nTest7. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest8. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s13)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest9. Hit "Enter" to try adding a duplicate student ')
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s8)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest10. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
print('  then print all 3 department student lists')
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
a, b = d1.addStudent(s10)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s11)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s12)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest11. Hit "Enter" to try to add s16 to ARTS, which will fail for low gpa, ')
print('    then add a new course grade of "A"/3 credits to s15, and try the add again.')
print('\nStudent to be added to ARTS is ', s16)      
a, b = d2.addStudent(s16)
print('\nResult of attempt to add ', s16.name, ' gpa: ', str(s16.gpa()), ' to ', d2.d_code)
print('\tis ', a, ', with reson code: ', b)


input('\n\n\n\nTest12. Adding 3 credit course with grade of "A" to ' + s16.name )
s16.addGrade("A", 3)
print('\nStudent profile is now: ', s16)
a, b = d2.addStudent(s16)
print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code:  ', b)
print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ', str(s16.gpa()))


input('\n\n\n\nTest13. Hit "Enter" to add s15 to ARTS.')
print('\nAttempting to add ', s15.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s15)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input ('\n\n\n\nT14Hit "Enter" to see the final student list for all departments')
print('\nNumber of students in ', d1.d_code, ' is ', len(d1.studentRoster))
d1.showStudents()
print('\nNumber of students in ', d2.d_code, ' is ', len(d2.studentRoster))
d2.showStudents()
print('\nNumber of students in ', d3.d_code, ' is ', len(d3.studentRoster))
d3.showStudents()      
print('\n\n\n***** End of A3 F23 Output **********')