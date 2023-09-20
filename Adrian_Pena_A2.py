class Student:
    totalEnrollment = 0
    g_num_counter = 0

    def __init__(self, name, major='IST', enrolled='y', credit=0, qpoints=0):
        self.name = name
        self.major = major
        self.enrolled = enrolled
        self.credit = credit
        self.qpoints = qpoints

        Student.totalEnrollment += 1
        self.g_num = f'G{str(Student.g_num_counter).zfill(5)}'
        Student.g_num_counter += 1

    def __str__(self):
        return (
            "Name: " + str(self.name) +
            ", Major: " + self.major +
            ", Enrolled: " + str(self.enrolled) +
            ", Credit: " + str(self.credit) +
            ", QPoints: " + str(self.qpoints)
        )

    def gpa(self):
        if self.credit == 0:
            return 0.0
        return self.qpoints / self.credit

    def addGrade(self, grade, credits):
        grade_values = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
        if grade in grade_values and 0 <= credits <= 4:
            qpoints = grade_values[grade] * credits

            self.credit += credits
            self.qpoints += qpoints
            return True
        else:
            return False

    def isActive(self):
        if self.enrolled.lower() == "y":
            return True
        elif self.enrolled.lower() == "n":
            return False

    def classLevel(self):
        if self.credit >= 90:
            return 'Senior'
        elif self.credit >= 60:
            return 'Junior'
        elif self.credit >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def eqStudent(self, other_student):
        if self.g_num == other_student.g_num and self.name == other_student.name:
            return True
        else:
            return False



# Global/executable code --------------------------------------

input('\nHit "Enter" to create several objects and print their summaries\n')

s1 = Student('David Miller', major = 'Hist',
      enrolled = 'y', credit = 0, qpoints = 0)           
s2 = Student('Emma Maria Vicente', major = 'Math',
      enrolled = 'y', credit = 90, qpoints = 315)
s3 = Student('A. Einstein', major = 'Phys',
      enrolled = 'y', credit = 0, qpoints = 0)           
s4 = Student('W. A. Mozart', major = 'Mus',
      enrolled = 'n', credit = 29, qpoints = 105)
s5 = Student('Emma Maria Vicente', major = 'CSci',
      enrolled = 'y', credit = 60, qpoints = 130)
s5.g_num = s2.g_num
s6 = Student('Vincent Van Gogh', major = 'Art',
      enrolled = 'y', credit = 120, qpoints = 315)
print('\nThe following Student objects were created: \n')
print('s1 = ', s1)
print('s2 = ', s2)
print('s3 = ', s3)
print('s4 = ', s4)
print('s5 = ', s5)
print('s6 = ', s6)
print('\nTotal number of students: ', Student.totalEnrollment)
input('\n\n\n Hit "Enter" to run several tests of the class methods -----------')
print('The gpa of ', s1.name, ' is ', s1.gpa(), '\n')
print('Class standing of ', s4.name, ' is ', s4.classLevel())
print('Class standing of ', s2.name, ' is ', s2.classLevel(), '\n')
if s1.eqStu(s2):
    print (s1.name, ' and ', s2.name, ' are the same student')
else:
    print (s1.name, ' and ', s2.name, ' are not the same student')
if s2.eqStu(s5):
    print (s2.name, ' and ', s5.name, ' are the same student')
else:
    print (s2.name, ' and ', s5.name, ' are not the same student\n')
if s1.isActive():
    print (s1.name, ' is currently active')
else:
    print (s1.name, ' is not currently active')
if s4.isActive():
    print (s4.name, ' is currently active')
else:
    print (s4.name, ' is not currently active\n')
print('Adding grade of "A" for ', s4.name, ', result: ', s4.addGrade('A', 3))
print('GPA of ', s4.name,' is now ', s4.gpa())
print('Class standing of ', s4.name, ' is now ', s4.classLevel())
print('\nTrying to add bogus grade of "X" to ', s1.name, ' result: ', s1.addGrade('X', 3))    
print('\nEnd of A2 Student class demo')