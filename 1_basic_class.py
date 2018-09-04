# basic class in python 3 and how to create objects
class Employees:
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
        
emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

print(emp_1.email)
print(emp_2.email)
