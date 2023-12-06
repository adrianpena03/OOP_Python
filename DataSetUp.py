#--------------------------------------------------------------------
# Data load/set up code follows - Fall 2024 (F2024) -----------------

from imports import selectMenu, Department, Person, Student, Faculty
from newClasses import University, Catalog, Course  

def DataSetUp ():
    print('\nStart of Department and Student class demo **************')
    # Set up student objects ---------------------------------------------
    print('\n1. Create student objects for use in the assignment ')
    s1 = Student('G34568', 'David Miller', '321 Maple Lane, Vienna, VA',
          '571-285-4567', 'dmiller8@gmu.edu',
          status = 'sophomore', major = 'Hist', enrolled = 'y',
          credits = 30, qpoints = 90)           
    s2 = Student('G21345', 'Sonia Fillmore', '123 Oak Street, Potomac, MD',
          '301-285-4567', 'sfillmor8@gmu.edu',status = 'senior', major = 'Math',
          enrolled = 'y', credits = 90, qpoints = 315)
    s3 = Student('G42156', 'Chris Squire', '4567 Park Lane, London, UK',
          '425-285-4567', 'csquire8@gmu.edu',status = 'sophomore', major = 'Musc',
          enrolled = 'y', credits = 45, qpoints = 160)
    s4 = Student('G10928', 'Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
          '524-485-5674', 'twilkenfeld@AU.gov',status = 'junior', major = 'Musc',
          enrolled = 'y', credits = 75, qpoints = 250)    
    s5 = Student('G22157', 'Larry Graham', '279 Yonge St., Toronto, On', 
          '416-987-5432', 'lgraham@gmail.com', status = 'senior', major = 'CHHS',
          enrolled = 'y', credits = 105, qpoints = 290)           
    s6 = Student('G31345', 'John Entwistle', '6 Stable Way, London, U.K.',
          '011-38-0123-1120', 'jwho@daltry.com', status = 'freshman', major = 'CSci',
          enrolled = 'y', credits = 15, qpoints = 35)
    s7 = Student('G44568', 'Esperanza Spalding', '2921 Westpark Dr, Mclean, VA',
          '703-560-8660', 'bassic@musician.org', status = 'junior', major = 'ARTS',
          enrolled = 'y', credits = 95, qpoints = 250)           
    s8 = Student('G55345', 'Tim Bogert', '92120 Ventura Hwy, Los Angeles, CA',
          '315-444-1944', 'Vfudge@atco.com', status = 'sophomore', major = 'Hist',
          enrolled = 'y', credits = 55, qpoints = 175)
    s9 = Student('G66113', 'Gordon Sumner', '925 Madison Ave., New York, NY',
          '212-926-4987', 'police@roxanne.com', status = 'freshman', major = 'Musc',
          enrolled = 'y', credits = 15, qpoints = 45)           
    s10 = Student('G11311', 'Paul McCartney', '62 Scotsman Way, Edinburgh, SC',
          '011-928-3835', 'pmac@gmu.edu', status = 'senior', major = 'ARTS',
          enrolled = 'y', credits = 110, qpoints = 275)
    s11 = Student('G22111', 'Elizabeth Smythe', 'PO Box 345, Almond City, PA',
          '215-926-4611', 'esmyth@gmu.edu', status = 'junior', major = 'ENGR',
          enrolled = 'y', credits = 85, qpoints = 250)
    s12 = Student('G31312', 'John McVie', '421 Lombard St., San Francisco, CA',
          '415-567-8901', 'fwoodmac@crown.org', status = 'sophomore', major = 'Hist',
          enrolled = 'y', credits = 45, qpoints = 120)
    # Set up faculty ----------------------------------------------------------
    f1 = Faculty('G98765', 'Gene Shuman', '3062 Covington Street, Fairfax, VA',
                 '571-235-2345', 'gshuman@gmu.edu', 'Assistant Professor', 'y',
                 18, 'teaching', 250000)     
    f2 = Faculty('G91299', 'Irina Hashmi', '123 Jermantown Road, Fairfax, VA',
                 '703-560-7890', 'ihashmi@gmu.edu', 'Assistant Professor', 'y',
                 18, 'teaching', 150000)
    f3 = Faculty('G01223', 'N. Lynn Gerber', '4421 River Road, Bethesda, MD',
                 '301-221-2736', 'nlgerber@gmu.edu', 'Professor', 'y',
                 12, 'teaching', 750000)
    f4 = Faculty('G00013', 'L. DaVinci', '4 Duomo Square, Florence, IT',
                 '011-102-8827', 'leonardo@louvre.net', 'Professor', 'y',
                 12, 'teaching', 15000)
    f5 = Faculty('G02234', 'Claude Monet', '23 rue de la Printemp, Giverny, FR',
                 '011-19-40-88-39-57', 'claudeimpression@mdorsay.com', 'Professor', 
                 'y', 12, 'teaching', 15000)
    f6 = Faculty('G00004', 'A. Turing', '9 Farsworth Green, Bletchley Park, UK',
                 '011-47-40-88-39-57', 'turingtest@ai.com', 'Professor', 
                 'y', 12, 'teaching', 950000)
    f7 = Faculty('G00222', 'W. Robeling', '977 River Drive, Brooklyn, NY',
                 '212-321-1885', 'bridge@brooklyn.com', 'Associate Professor', 
                 'y', 6, 'teaching', 1950000)
    print('\nList of Student objects created -------------------------------: ')
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
    print('s11= ', s11)
    print('s12= ', s12)

    print('\nList of Faculty objects create ---------------------------------: ') 
    print('f1= ', f1)
    print('f2 = ', f2)
    print('f3 = ', f3)
    print('f4 - ', f4)
    print('f5 = ', f5)
    print('f6 = ', f6)
    print('f7 = ', f7)
    # Set up departments ----------------------------------------------------
    d1 = Department('ENGR', 'Engineering', 5, 2.75)
    d2 = Department('ARTS', 'Art and Architecture', 15, 2.0)
    d3 = Department('CHHS', 'College of Health and Human Sevrices', 10, 2.5)
    d4 = Department('BEng', 'Bioengineering', 5, 2.65)

    input('\n2. Hit "Enter" to see the list of departments created ')
    print('\n\nDepartments established-------------------------:')
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    depts = [d1, d2, d3, d4]

    input('\n\n\n\n3. Hit "Enter" to add Student objects to various departments\n')
    d1.addStudent(s1)      
    d1.addStudent(s2)
    d1.addStudent(s3)
    d2.addStudent(s4)
    d3.addStudent(s5)
    d4.addStudent(s6)
    d2.addStudent(s7)
    d4.addStudent(s8)
    d3.addStudent(s9)
    d4.addStudent(s10)
    d2.addStudent(s11)
    d1.addStudent(s12)
    d1.addFaculty(f1)
    d1.addFaculty(f2)
    d3.addFaculty(f3)
    d2.addFaculty(f4)
    d2.addFaculty(f5)
    d4.addFaculty(f6)
    d1.addFaculty(f7)

    print('\nPrint the list of students by Department ')
    for r in (d1, d2, d3, d4):
        print('\n', r.getName() + ' Department ')    
        r.printRoster('s')
    print('\nPrint the list of faculty by Department ')
    for r in (d1, d2, d3, d4):
        print('\n', r.getName() + ' Department ')    
        r.printRoster('f')
     
    # Create the single University object "GMU"
    GMU = University( )
    # Add departments to University object 'GMU'
    GMU.addDept(d1)
    GMU.addDept(d2)
    GMU.addDept(d3)
    GMU.addDept(d4)
    # Create and add Catalog object 'F2024' to University object 'GMU'
    F2024 = Catalog('Fall 2024')
    GMU.addCat(F2024)
    # Add Student objects to University object 'GMU'
    GMU.addStudent(s1)
    GMU.addStudent(s2)
    GMU.addStudent(s3)
    GMU.addStudent(s4)
    GMU.addStudent(s5)
    GMU.addStudent(s6)
    GMU.addStudent(s7)
    GMU.addStudent(s8)
    GMU.addStudent(s9)
    GMU.addStudent(s10)
    GMU.addStudent(s11)
    GMU.addStudent(s12)

    input ('\nEnd of data set up. Hit "Enter" to start application')

    return GMU, F2024
    
