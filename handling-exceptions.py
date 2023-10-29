
# There are 4 important keywords that come to play with it comes to handling exceptions.
# They are: "try", "except", "else", and "finally".

# The "try" block lets you test a block of code for errors.
# The "except" block lets you handle the error. It defines what should happen should the error occur.
# The "else" block lets you execute code when there is no error. It defines what should happen if there is no error.
# The "finally" block defines what should happen regardless of the result of the try- and except blocks. (What should happen whether or not there is an error)

                                          
#                                                  ILLUSTRATION
#                                         --------------------------------

try:
    file = open("a_file.txt")                         # The try block test whether it is possible to open that file (whether the file exists)
except FileNotFoundError:                             # This except block specifies what happen in case of a 'FileNotFoundError'.
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:                     # We use the 'as' keyword to get hold of the error message
    print(f"The key {error_message} does not exist")  # and print it dynamically so as to give more clarity
else:
    content = file.read()
    print(content)
finally:
    file.close()                                      # We close the file whether there was an exception or not
    print("File closed")



                                                   RAISING EXCEPTIONS
                                         -----------------------------------------
# In addition to the "try", "except", "else", and "finally" keywords, there is the "raise" keyword which can be used to raise an exception
# if a condition occurs. 
# We may want to do this in a situation where certain entries may not be caught by the code but are valid entry but logically incorrect.
# Example: The program below calculates users' bmi based on height and weight entered. If a user entered a height of 20 (maybe their age
# instead) the code will not catch such errors but in reality human height cannot exceed 4 meters.
# As such, we raise an exception in case entry for height is greater than or equal to 4 meters

height = float(input("height: "))
weight= int(input("weight: "))

if height > 4:
    raise ValueError("Human height cannot exceed 4 meters")     # We must specify the error type to be raised, and can optionally include
                                                                # a message to be printed when the error is raise
bmi = weight / (height * height)
print(bmi)
