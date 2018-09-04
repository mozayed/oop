# using property attribute like getters and setters
# usning the property attribute @property allowed us to still call the email
# as an attribute not as method, meaning without () so no change required in code

class Employees:
          
    def __init__(self, first, last):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
     
    # use property decorator
    @property
    def email(self):
        return '{}.{}@mycompany.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employees('John','Smith')

# if we change the first name manually
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)