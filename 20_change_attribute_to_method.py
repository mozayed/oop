# changing the email from attribute to a method to avoid the conflict between the passed
# arguments and current arguments

class Employees:
          
    def __init__(self, first, last):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
     
    # we can use email as a method
    def email(self):
        return '{}.{}@mycompany.com'.format(self.first, self.last)
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employees('John','Smith')

# if we change the first name manually 
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email())  # added () here
print(emp_1.fullname())