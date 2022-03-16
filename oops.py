class Employee:

    increment = 1.5 
    no_of_employees = 0
    def __init__(self,fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1

    def increase(self):
        self.salary = int(self.salary * Employee.increment)


# amit = Employee('Amit','Yadav  ',50000)
# kumar = Employee('Kumar','bhai',50000)
# print(amit.fname, kumar.fname)
#---------------------------------------------------
# amit = Employee('Amit','Yadav  ',50000)
# kumar = Employee('Kumar','bhai',50000)
# print("Actuall salary - ",amit.salary)
# amit.increase()
# print("After increase salary - ",amit.salary)
#-----------------------------------------------------
# amit = Employee('Amit','Yadav  ',50000)
# kumar = Employee('Kumar','bhai',50000)
# print(amit.__dict__) # instaint all variable show
# amit.increment = 9
# print(amit.__dict__)
#-----------------------------------------------------
# amit = Employee('Amit','Yadav  ',50000)
# kumar = Employee('Kumar','bhai',50000)
# print(Employee.__dict__) # Employee all variable 
#-----------------------------------------------------
# -------------------No_of_Employee ?
# print("Befor - ",Employee.no_of_employees)
# amit = Employee('Amit','Yadav  ',50000)
# kumar = Employee('Kumar','bhai',50000)
# print("After - ",Employee.no_of_employees)

#-#------------------------------------------------------
# @classmethod
# def change_increment(cls,amount):
#     cls.increment = amount

# amit = Employee('Amit','Yadav  ',50000)
# kumar = Employee('Kumar','bhai',60000)

# print(amit.salary)
# Employee.change_increment(2)
# amit.increase()
# print(amit.salary)  

#---------------------------------------------------

@classmethod
def from_str(cls,emp_st)
