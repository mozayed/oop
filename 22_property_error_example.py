# using property attribute like getters and setters
class Employees:
          
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
     
    # use property decorator
    @property
    def email(self):
        return '{}.{}@mycompany.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employees('John','Smith',40000)


# this will give error as you cannot set it here
emp_1.email = 'a.b@email.com'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)