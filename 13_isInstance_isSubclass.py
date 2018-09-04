# is instance and is subclass

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

# here using the developer class raise amount
class Developer(Employees):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
            # use the base class to initiate the init method
            super().__init__(first, last, pay)
            #Employees.__init__(self, first, last, pay) # we can use this syntex too
            self.prog_lang = prog_lang
            
class Manager(Employees):
    
    def __init__(self, first, last, pay , employees_supervise = None):
        super().__init__(first, last, pay)
        if employees_supervise is None:
            self.employees_supervise = []
        else:
            self.employees_supervise = employees_supervise
            
     
    def add_emp(self,emp):
        if emp not in self.employees_supervise:
            self.employees_supervise.append(emp)
            
    def rem_emp(self,emp):
        if emp in self.employees_supervise:
            self.employees_supervise.remove(emp)  
            
    def print_emps(self):
        for emp in self.employees_supervise:
            print('---->', emp.fullname())
        
emp_1 = Developer('John','Smith',80000, 'Python')
emp_2 = Developer('Sally','Johnson',45000, 'Java')

mgr1 = Manager('Mike', 'Brown', 120000,[emp_1])

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Developer))
print(isinstance(mgr1, Employees))

print(issubclass(Manager, Employees))
print(issubclass(Developer, Employees))
print(issubclass(Developer, Manager))