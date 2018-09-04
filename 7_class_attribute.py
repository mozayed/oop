# create an attribute that can be changed only from class and any changes from any instance 
# will not affect other instances

class Employees:
    
    raise_amount = 1.04
    nump_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
        
        Employees.nump_of_emps +=1 #no need to use self as we don't need instances to change it
     
    # regular method in a class which takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # we can use Employees.raise_amount

emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

emp_1.nump_of_emps = 4
print(emp_2.nump_of_emps)
print(Employees.nump_of_emps)
print(emp_1.nump_of_emps)