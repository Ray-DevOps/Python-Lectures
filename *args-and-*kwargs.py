
                                                 *args
                                           ----------------------

# In Python, it is possible to make a function flexible so as to allow any number of arguments to be used as input.
# In that case, you would use *args. In that case, you can pass in any number of arguments when calling the function
# and the arguments passed would be in the form of a tuple.

Example:
----------------
                                             
def add(*args):
    print(sum(args))

add(1, 2, 3, 4)        ----------->   10           

