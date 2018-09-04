# change class variable value

class Employees:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
        
     
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # we can use Employees.raise_amount

emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

#change the class variable
#Employees.raise_amount = 1.05

#change the class variable from the instance
emp_1.raise_amount = 1.05

print(Employees.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
