#----------------------------------------------------------------------
# newClasses .py module...Instuctions to Students working on A8
#
# Students must complete the methods in the classes below to make the
# University course creation application work correctly.
#
# The methods to be completed have a 'provide code ' comment to the
# right of their signature lines.  They also have a coded number
# associated with each method to be completed. The code replaces the
# "pass" statements in each, but in most cases is more than one line.
#---------------------------------------------------------------------

#--------------------------------------------------------------------
# University - University class - container for Department objects
#                                 and Catalog objects 
# Only one object for A8, but could hold other university objects
#
# Author:  Gene Shuman      11/13/2023  
#---------------------------------------------------------------------

from imports import Department, Person, Student, Faculty

class University():
    """ University class - creates University objects, one for A8. 
        Container for Department, catalog, and student objects
        ---------------------------------------------------------- """
    
    def __init__(self, name = 'GMU'):
        self.__name = name
        self.__departments = [ ]   # container for Department objects
        self.__catalogs = [ ]      # container for catalogs
        self.__students = [ ]      # roster of all univ. student objects
 
    def __str__(self):
        return('UNIVERSITY STR METHOD: University name: ' + self.__name + ', contains ' +
               str(len(self.__departments))+ ' departments ')

    def getName(self):          # U1. provide code for this method.
        """Input: none
           Return: name (string) of University object.
        """
        return self.__name
    
    def addDept(self, d_obj):   # U2. provide code for this method.
        """Add Department object to the 'departments' container list.
           Input: Department object
           Return: none
        """
        if isinstance(d_obj, Department):
            self.__departments.append(d_obj)

    
    def addCat(self, c_obj):   # U3. provide code for this method
        """Input: Catalog object
           Add the input Catalog object to the 'catalogs' container list.
           Return: none
        """
        if isinstance(c_obj, Catalog):
            self.__catalogs.append(c_obj)
 

    def addStudent (self, s_obj):  # U4. provide code for this method
        """Input: Student object
           Add the input Student object to the 'students' cotainer list.
           Return: none
        """
        if isinstance(s_obj, Student):
            self.__students.append(s_obj)


    def __len__(self):
        return len(self.__departments)

    def __contains__(self, u_obj):
        if isinstance(u_obj, Department):
            for d in self.__departments:
                if d.d_code == u_obj.d_code:
                    return True
            return False
        if isinstance(u_obj, Catalog):
            for c in self.__catalogs:
                if c.__name == u_obj.__name:
                    return True
            return False
        
    def listDepts(self):    # U5. provide code for this method
        """Input: none
           Return: a list of all Department objects in container.
        """
        return self.__departments


    def listStudents(self): # U6. provide code for this method
        """Input: none
           Return: a list of all Student objects in container.
        """
        return self.__students

 
    def printDepts(self):
        for d in self.__departments:
            print(d)

#--------------------------------------------------------------------
# Course - Course class - course objects
#
# Author:  Gene Shuman      11/13/2023  
#---------------------------------------------------------------------
class Course():
    """ Course class - creates Course objects - created by A8 appl.
                     - container for students registered for course
        Attributes:  d_code from Department object + number + title
                     name of Faculty object instructor
                     container list of assigned Student objects
                     in course.
        ---------------------------------------------------------- """
    
    def __init__(self, d_code, number, title, instructor):
        self.__d_code = d_code
        self.__number = number
        self.__section = '001'  # Only one section per course (KISS)
        self.__title = title    # descriptive course title
        self.__instructor = instructor
        self.__students = [ ]   # container for Student objects
 
    def __str__(self):  # Co1: provide code for this method
        """Return a string that is a good print/display representation
           of the course object.  Include the code, number, section,
           instructor, and number of students.
           Example:
           Course: ENGR-101.001 - Introduction to Engineering
                                  Instructor: A. Einstein
                                  11 students registered          """
        return (f"Course: {self.__d_code}-{self.__number}.{self.__section} - {self.__title}\n"
                f"Instructor: {self.__instructor}\n"
                f"{len(self.__students)} students registered")


    
    def addFaculty (self, f_obj):  # Co2. provide code for this method
        """Input: Faculty object
           Assign name (string) of faculty belonging to the input object
                   to self.__instructor.
           Return: True to signify successful assignment
        """
        if isinstance(f_obj, Faculty):
            self.__instructor = f_obj.getName()
            return True
        else:
            return False


    def addStudent (self, s_obj):  # Co3. provide code for this method
        """Input: Student object
           Add input Student object to the course student container.
           Return: True to signify successful add
        """
        if isinstance(s_obj, Student):
            self.__students.append(s_obj)
            return True
        else:
            return False


    def getName (self): # Co4. provide code for this method
        """Input: none
           Return: course dept code + number (e.g. ENGR-101) as string. """
        return f"{self.__d_code}-{self.__number}"


    def __len__(self):
        return len(self.__students)

    def __eq__(self, c_obj):
        if self.__d_code == c_obj.__d_code and self.__number == c_obj.__number:
            return True                                                                                                                                               
        return False

    def printStudents(self):  # Co5. provide code for this course
        """Input: none
           Print/display the students in the course. Use the Student
               '__str__' method that works with the Python 'print' function.
           Return: none
        """ 
        for student in self.__students:
            print(student)

    
#--------------------------------------------------------------------
# Course - Catalog - Catalog object - contains Course objects
#                    Only one needed for A8
#
# Author:  Gene Shuman      04/23/2020  
#---------------------------------------------------------------------
class Catalog():
    """ Catalog class - creates Catalog object - created by A8 appl.
                     - container for courses for a given semester+year
        Attributes:  name - e.g. S2021 is Spring 2021 semester
                     course list - object refs. of all courses in 
                     catalog.
        ---------------------------------------------------------- """
    
    def __init__(self, name):
        
        self.__name = name
        self.__courses = [ ]   # container for Course objects
        
 
    def __str__(self):
        return 'CATALOG STR METHOD: Catalog: ' + self.__name + ' - ' + str(len(self.__courses)) + ' courses'

    def getName (self):    # Ct1. provide code for this method
        """Input: none
           Return: name of Catalog (string).
        """
        return self.__name

    
    def addCourse (self, c_obj):  # Ct2. provide code for this method
        """Input: Course object
           Add the input Course object to the catalog 'courses'
               container list.
           Return: True to signify successful add
        """
        if isinstance(c_obj, Course): # wondering if i should use isinstance here
            self.__courses.append(c_obj)
            return True
        else:
            return False
               
    def __len__(self):
        return len(self.__courses)

    def __contains__(self, c_obj):   # Ct3. provide code for this method
        """Input: Course object           
             (This 'dunder' method uses 'Duck typing' to provide functionality
              for the application code to use the 'in' keyword to ask whether
              a course object is in the catalog.)
           Return: True if c_obj found in catalog, otherwise return False.
        """
        if c_obj in self.__courses:
            return True
        else:
            return False
 

    def printCatalog(self): # Ct4. provide code for this method
        """Input: none
           Print a list of all Course objects in the catalog 'courses'
           container list.  Use the Course class '__str__' method that
           works with the Python 'print' function.
           Return: none
        """
        for course in self.__courses:
            print(course)
            

    def listCourses(self):  # Ct5. provide code for this method
        """Input: none
           Return a list of all course objects in the catalogs 'courses'
           container list.                                        """
        return self.__courses




    
