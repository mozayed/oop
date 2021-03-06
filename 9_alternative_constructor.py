# having a special case when receive the instance attributes in a text with - between them
# so we use split on the - to create the instances
class Employees:
    
    raise_amount = 1.04
    nump_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first #i can use self.anyname but we like to stick to argument name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
        
        Employees.nump_of_emps +=1 #no need to use self as we don't need instances change and refelct changes
     
    # regular method in a class which takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # we can use Employees.raise_amount
        
    # using a class method
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

emp_1 = Employees('John','Smith',80000)
emp_2 = Employees('Sally','Johnson',45000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-65000'
emp_str_3 = 'Jack-Donhue-85000'

first,last,pay = emp_str_1.split('-')
new_emp_1 = Employees(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)