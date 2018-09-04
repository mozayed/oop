# change attribute values after object initialization
class Employees:
          
    def __init__(self, first, last):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
     
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employees('John','Smith')

# if we change the first name manually here and tried to print we see that email didnt change
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())