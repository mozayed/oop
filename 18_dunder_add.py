# Using the Dunder add __add__ to represent adding two instances together
# Using the Dunder __len__
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
    
    # now when we print the instance we have it represnted that way
    def __repr__(self):
        return "Employees('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # now it is using this format when printing the instance
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    # self and other are both instances
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        # actually it is as print('test'.__len__())

emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

print(emp_1 + emp_2)

print(len(emp_1))