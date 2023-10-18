
                   # INSTANCE VARIABLES VERSUS CLASS VARIABLES
                  ---------------------------------------------------

# - Instance variables are those set individually for each instance
# - Instance variables are unique for each instance, such as name, email, pay
# - Class variables are those shared by all instances of the class
# - Class variables are the same for each instance. e.g. bonus rate

# Though class attributes are set at the class level, they can also be accessed at the instance level.

class Item:

    discount_rate = 0.2                                              # We create a class attribute

    def __init__(self, name: str, price: float, quantity=0):

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", -100, -1)

item2 = Item("Laptop", -1000, -3)


print(Item.discount_rate)          ---------->  0.2                # Attribute (discount_rate) is accessible from the class
print(item1.discount_rate)         ---------->  0.2                # Attribute (discount_rate) is also accessible from the the instance (object) item1
print(item2.discount_rate)         ---------->  0.2                # Attribute (discount_rate) is also accessible from the the instance (object) item2


############################################################################################


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

