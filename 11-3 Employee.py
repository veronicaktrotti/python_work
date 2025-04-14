class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

emp1 = Employee("Veronica", "Trotti", 62500)
print(emp1.first_name) 
print(emp1.last_name)        
print(emp1.annual_salary)    

def give_raise(self, amount=5000):
     self.annual_salary += amount
     print(f"New annual salary: {self.annual_salary}")
