import datetime as dt

"""

This code defines a Python Employee class to represent employee information, 
including ID, name, birthdate, job title, and salary. It calculates hourly rates, ages, 
and retirement eligibility, demonstrating data management for employees.

CREATED BY ADRIAN PENA

"""

class Employee():
    def __init__(self, employee_id, name, birth_year, birth_month, job_title, annual_salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__job_title = job_title
        self.__annual_salary = annual_salary

    def __str__(self):
        return (
            "Employee ID: " + str(self.__employee_id) +
            " - Name: " + self.__name +
            " - Birth Year: " + str(self.__birth_year) +
            " - Birth Month: " + str(self.__birth_month) +
            " - Job Title: " + self.__job_title +
            " - Annual Salary: " + str(self.__annual_salary)
        )

    def hourly_rate(self):
        hourly = float(int(self.__annual_salary) / 2080)
        rounded = float(round(hourly, 2))
        return rounded

    def age(self):
        curr_time = dt.datetime.now().__str__()
        curr_year = int(curr_time[0:4])
        if self.__birth_month > curr_year:
            return curr_year - self.__birth_year - 1
        else:
            return curr_year - self.__birth_year

    def can_retire(self):
        if self.__age() > 70:
            return True
        else:
            return False




print('\nStart of Employee class demo')
e1 = Employee()._get('E34568', 'David Miller', 1996, 1, 'Accountant', 82000)
e2 = Employee()._get('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
e3 = Employee()._get('E43344', 'Chase Snidley', 1992, 8, 'Salesman', 75000)
e4 = Employee()._get('E12157', 'Roone Arledge', 1979, 11, 'Lawyer', 92000)
e5 = Employee()._get('E00001', 'Abe Lincoln', 1940, 2, 'Former POTUS', 85000)
print('e1 = ', e1)
print('e2 = ', e2)
print('e3 = ', e3)
print('e4 = ', e4)
print('e5 = ', e5)
print('Hourly rate for ', e1.name, ' is ', e1.hourly_rate())
print('Age of ', e1.name, ' is ', e1.age())
print('Age of ', e3.name, ' is ', e3.age())
print('Job description of ', e4.name, ' is ', e4.job_title)
print('Retirement eligibility for ', e2.name, ' is ', e2.can_retire())
print('Retirement eligibility for ', e5.name, ' is', e5.can_retire())
print('\nEnd of Employee class demo')
