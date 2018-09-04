# adding methods to the class

class Employees:
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
     
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    
emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

print(Employees.fullname(emp_2)) # call the method on the class and passing the instance as an argument
print(emp_1.fullname())
	