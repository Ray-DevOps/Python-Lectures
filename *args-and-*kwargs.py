

############################################## USING *args AND *kwargs IN A FUNCTION #################################################


                                                 *args
                                           ----------------------

# In Python, it is possible to make a function flexible so as to allow any number of non-keyworded arguments to be used as input.
# In that case, you would use *args to pass in any number of arguments when calling the function
# and the arguments passed would be in the form of a tuple.

Example1:
----------------
                                             
def add(*args):
    print(sum(args))

add(1, 2, 3, 4)        ----------->   10           


Example2:
----------------

def add(*args):
    squares = [ ]
    for n in args:                # The arguments entered for *args form a tuple, and as such we can 
        n = n * n                 # loop through just as we can any other tuple
        squares.append(n)
    print(squares)           ----------->  [1, 4, 9, 16]
    print(args)              ----------->  (1, 2, 3, 4)  

add(1, 2, 3, 4)       
    

                                                 *args
                                           ----------------------

# While we use *args to pass in any number of non-keyworded arguments in a function, we can use **kwargs to pass in any number of
# keyword arguments in a function. When calling the function, the keyword arguments passed would be in the form of a dictionary.
# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. 
# That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.


Example1:
--------------
def myFun(*args, **kwargs):        # Now we can use both *args ,**kwargs. Python would distinguish the non-keyword arguments (args) from the keyword arguments(kwargs)
    
    print("args: ", args)                -------------->     args:  ('geeks', 'for', 'geeks')                             # printed as args because they are not keyworded 
    print("kwargs: ", kwargs)            -------------->     kwargs:  {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}   # printed as kwargs because they are keyworded          

myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


                                             
Example2:
-------------
def calculate(n, **kwargs):
    n += kwargs["add"]                          # kwargs["add"] with give the value of the 'add' key in the dictionary. Therefore this line of code gives 2 += 3
    n *= kwargs["multiply"]                     # kwargs["multiply"] with give the value of the 'multiply' key in the dictionary. Therefore this line of code gives 2 *= 5
    print(n)                  ------------>    25
    print(kwargs)             ------------>  {'add': 3, 'multiply': 5}

calculate(2, add=3, multiply=5)
                                      

############################################## USING *args AND *kwargs IN A CLASS #################################################



Example1 (*args in classes):
-------------------------------

class Car():

    def __init__(self, *args):
        self.speed = args[0]                   # defining the speed (of any object created) as the first argument passed (Remember args is a tuple)
        self.color = args[1]                   # defining the color (of any object created) as the second argument passed

audi = Car('200mph', 'red')                    # creating objects of car class    
bmw = Car('250mph', 'black')

print(audi.color)    ------->    red           # 'red' was the second argument passed when creating the audi object from the Car class
print(bmw.speed)     ------->    250mph        # '250mph' was the first argument passed when creating the bmw object from the Car class




Example2 (*kwargs in classes):
--------------------------------

class Car():
    def __init__(self, **kwargs):

        self.speed = kwargs['s']               # defining the speed (of any object created) as the value of the 's' key (Remember kwargs is a dictionary)
        self.color = kwargs['c']               # defining the color (of any object created) as the value of the 'c' key

audi = car(s='200mph', c='red')                # creating objects of Car class
bmw = car(s='250mph', c='black')

print(audi.color)    ------->    red           # 'red' was the value of the 'c' key in the keyword arguments passed when creating the audi object from the Car class
print(bmw.speed)     ------->    250mph        # '250mph' was the value of the 's' key in the keyword arguments passed when creating the bmw object from the Car class



Example3 (*kwargs in classes):
--------------------------------

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]                   # Note that kwargs["make"] can also be written as kwargs.get("make")
        self.model = kwargs["model"]                 # We can access values of dictionary keys in any of both ways


my_car = Car(make="Mercedes Benz", model="GLC AMG Coupe")

print(my_car.make)                                               ----------->     Mercedes Benz
print(my_car.model)                                              ----------->     GLC AMG Coupe
print(f"I just bought my new {my_car.make} {my_car.model}")      ----------->     I just bought my new Mercedes Benz GLC AMG Coupe

