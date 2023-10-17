# INSTANCE VARIABLES VERSUS CLASS VARIABLES

# - Instance variables are those set individually for each instance

# - Instance variables are unique for each instance, such as name, email, pay

# - Class variables are those shared by all instance of a Class

# - Class variables are the same for each instance. e.g. bonus rate


class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@companyltd.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def bonus_pay(self):
        return int(self.pay * 0.05)


employee1 = Employee("jenny", "corey", 50000)
employee2 = Employee("roger", "moore", 60000)


print(employee1.bonus_pay())     ------------->   2500
print(employee2.bonus_pay())     ------------->   3000

# Though the Class variable apply to all instances in a Class, you can optionally change the variable for
# a particular instance.

