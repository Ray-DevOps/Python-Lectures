# Inheritance allows a sub-class to inherit attributes and methods from a parent class.
# As such the sub-class would simply inherit all the functionalities of the parent class, thereby avoiding the need
# to re-write code.

# The sub-class can then add or modify attributes and methods without affecting the functionality of the parent class.
# Assuming that we have an "Employee" class already created with all it's methods and now we want to create a sub-class
# say for developers


###################################################### ILLUSTRATION 1 #################################################


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@companyltd.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def bonus_pay(self):
        return float(self.pay * 0.05)

class Developer(Employee):                               # The parenthesis indicates that the Developer class is a sub-class of  
    pass                                                 # (inherits from) the parent class
                                                         # Even though the Developer class has no code of its own (only has the "pass" 
                                                         # statement, it can still perform all the functionalities of the parent class
employee1 = Employee("jenny", "corey", 50000)
employee2 = Employee("roger", "moore", 60000)

developer1 = Developer("michael", "hardman", 80000)
developer2 = Developer("amy", "carn", 90000)

print(employee1.email)                 ------->      jenny.corey@companyltd.com
print(employee2.bonus_pay())           ------->      3000.0

print(developer1.email)                ------->      michael.hardman@companyltd.com
print(developer2.bonus_pay())          ------->      4500.0



###################################################### ILLUSTRATION 2 #################################################


# We can customize the methods and attributes of the sub-class to override what's given in the parent class. 
# In our example, suppose we want developers to earn a 10% bonus while other regular employees only earn a 5% bonus, 
# we would simply have to create a custom bonus method in the Developer class and that will override the bonus
# method of the Employee (parent) class when calculating the bonus to developers.

class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@companyltd.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def bonus_pay(self):
        return float(self.pay * 0.05)

class Developer(Employee):
    def bonus_pay(self):
        return float(self.pay * 0.10)


print(employee1.email)                 ------->      jenny.corey@companyltd.com
print(employee2.bonus_pay())           ------->      3000.0         # employee bonus is only 5% as determined by the parent method

print(developer1.email)                ------->      michael.hardman@companyltd.com
print(developer2.bonus_pay())          ------->      4500.0         # developer bonus is only 10% as determined by the sub-class method                       




###################################################### ILLUSTRATION 3 #############################################################


# Suppose you want the sub-class to have more attributes or an attribute that doesn't exist in the parent class, you'd need to use
# the init method under the sub-class to initialize a function.

# Following from our examples above, suppose we want to add a programming language attribute for developers, but not for other
# employees. 


#   ************* code for parent class as above comes here  ******************

class Developer(Employee):

    def __init__(self, first_name, last_name, pay, prog_lang):        # init method in sub-class allows us to introduce a new attribute
        Employee.__init__(self, first_name, last_name, pay)           # The "Employee.__init__" allows the parent to handle the existing attributes so we don't have to copy the entire code
        self.prog_lang = prog_lang                                    # Now we introduce our new attribute "prog_lang" inside the sub-class
      
    def bonus_pay(self):
        return float(self.pay * 0.10)


print(developer2.email)          ------->    amy.carn@companyltd.com
print(developer1.prog_lang)      ------->    Python



###################################################### ILLUSTRATION 4 #########################################################


# We can also introduce loops and if/else statements when defining attributes within a method. Following from our examples above,
# we can create another method called Manager, and introduce a new attribute called "subordinates" which indicates the number of
# people who report to the manager.


#   ************* code for parent class as above comes here  ******************

class Manager(Employee):

    def __init__(self, first_name, last_name, pay, subordinates=None):     # We set a default value for no. of subordinates to None instead of a empty list
        Employee.__init__(self, first_name, last_name, pay)                # because it is not advisable to pass mutable data types as default arguments
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

  
    def add_subordinates(self, subords):                   # This method allows us to add subordinates under a manager
        if subords not in self.subordinates:
            self.subordinates.append(subords)

  
    def remove_subordinates(self, subords):                # This method allows us to remove subordinates from under a manager
        if subords in self.subordinates:
            self.subordinates.remove(subords)

  
    def print_subordinates(self):                          # This method allows us to print the full name of all subordinates under a manager
        for subords in self.subordinates:
            print(subords.full_name())

  
    def bonus_pay(self):                                   # A custom function to award managers a bonus of 15%
        return float(self.pay * 0.15)


developer1 = Developer("michael", "hardman", 80000, "Python")
developer2 = Developer("amy", "carn", 90000, "Java")

manager1 = Manager("Sue", "Smith", 110000, [developer1])   # Creating manager1 object and adding developer2 under her

print(manager1.email)                  ------->     Sue.Smith@companyltd.com
manager1.print_subordinates()          ------->     michael hardman

manager1.add_subordinates(developer2)                # This adds developer2 under manager1
manager1.remove_subordinates(developer1)             # This removes developer1 from under manager1

manager1.print_subordinates()           ------->     amy carn



########################################## isinstance and issubclass #########################################################


# isinstance is a Python built-in function that will tell us if an object is an instance of a class

print(isinstance(manager1, Manager))  ------->  True      #  Meaning "manager1" is an instance (object) of the "Manager" class
print(isinstance(manager1, Developer)) ------->  False    #  Meaning "manager1" is NOT an instance (object) of the "Developer" class


# isinstance is a Python built-in function that will tell us if a class is a sub-class of another class

print(issubclass(Developer, Employee))  ------->  True    #  Meaning "Developer" is a sub-class of the "Employee" class
print(issubclass(Developer, Manager))   ------->  False   #  Meaning "Developer" is not a sub-class of the "Manager" class



















