# Class Variables, a need to have a class variable to replace the 4% pay increase and make it dynamic

class Employees:
    
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
     
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

# printing the base pay of employee1
print(emp_1.pay)
# applying the raise
emp_1.apply_raise()
# printing the new base pay of employee1
print(emp_1.pay)