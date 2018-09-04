# use class inheritance

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

# even without any code, the instances of Developer class can do anything in the Employees class
class Developer(Employees):
    pass
        
emp_1 = Developer('John','Smith',80000)
emp_2 = Developer('Sally','Johnson',45000)

print(emp_1.email)
print(emp_2.email)