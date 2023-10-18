# We could create a variable that would be incremented by 1 each time we create a new object with the class.

class Employee:

    num_of_employees = 0                                        # here we define the variable and set its value to 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@companyltd.com"

        Employee.num_of_employees += 1                          # Here we we specify that the value of the variable ne increased
                                                                # by 1 each time we create a new object with the class
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def bonus_pay(self):
        return float(self.pay * 0.05)

print(Employee.num_of_employees)  ---------------> 0            # We haven't created any employees yet. So the variable value is 0
                                                                
employee1 = Employee("jenny", "corey", 50000)                   # Here we create our first employee "Jenny Corey"                 
employee2 = Employee("roger", "moore", 60000)                   # Here we create our second employee "Roger Moore"  

print(employee1.bonus_pay())                                     
print(employee2.bonus_pay())

print(Employee.num_of_employees)  ---------------> 2            # So the variable value now is 2 (two objects created with the Class)

