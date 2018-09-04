# using setters as same name of attribute.setter
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
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employees('John','Smith')

emp_1.fullname = 'Mike Brown'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)