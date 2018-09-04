# use static methods which are not directly related to any data with the class or the instance
# so if you don't need to access the class or the instance inside the method then it should be
# a static method

class Employees:
    
    raise_amount = 1.04
    nump_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
        
        Employees.nump_of_emps +=1 #no need to use self as we don't need instances change and refelct changes
     
    # regular method in a class which takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # we can use Employees.raise_amount
        
    # using a class method
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_string):
        first,last,pay = emp_string.split('-')
        return cls(first, last, pay)
    
    # use static methods which neither take the class nor the instance as an argument
    @staticmethod
    def is_workday(day):
        return day.weekday() != 5 or day.weekday() != 6

emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

import datetime
mydate = datetime.date(2018,8,8)
print(Employees.is_workday(mydate))