

####################################################   SIMPLE LIST COMPREHENSION   #################################################


# Given a list of numbers as follows and  

original_list = [1, 2, 3]

# Suppose we want to create a new list which takes the numbers in the riginal list and multiply by 2, we could do the following:

new_list = [ ]     # First we define an empty list called new_list

for n in original_list:
  n = n * 2
  new_list.append(n)       

print(new_list)         -------------->         [2, 4, 6]

# Alternatively, we could achieve the same results with list_comprehension, which summarizes the 4 lines of code into a single
# line of code, as follows. 


new_list = [n * 2 for n in original_list]             # i.e.   new_list = ['new_item' for 'each_item' in 'original_list']

print(new_list)         -------------->         [2, 4, 6]

# Note that the concept of list comprehension can also be applied to other data types like strings and tuples.



####################################################   CONDITIONAL LIST COMPREHENSION   #################################################



# We can add conditions to list comprehension. See example below


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]

print(short_names)          -------------->              ['Alex', 'Beth', 'Dave']        


long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)           -------------->              ['CAROLINE', 'ELEANOR', 'FREDDIE']



####################################################   ADAVANCED LIST COMPREHENSION   #######################################################


# Suppose we're presented with 2 text files file1.txt and file2.txt, and each of these files contain a list of numbers (numbers in
# text files are strings), and we're asked to print out a python list (called "result") containing numbers that are common to both files.
# The numbers in result shoulf be of type integer.


file1 = open("file1.txt", "r")
data1 = file1.read()
file1_list = data1.split("\n")

file2 = open("file2.txt", "r")
data2 = file2.read()
file2_list = data2.split("\n")

result = [int(num) for num in file1_list if num in file2_list and num.isdigit() == True]

print(result)



###########################################################   DICTIONARY COMPREHENSION   ################################################################


# Dictionary comprehension allows us to create a new dictionary from the values in a list or in a dictionary.

new_dict = {new_key:new_value for each_item in original_list}


# We could also create a new dictionary based on the values in an existing dictionary. Here, we would take the original dictionary, get hold of
# all the items in the dictionary and split it into keys and values, and use them to create new key/value pairs.
# Just like with list comprehension, we can apply conditions to dictionary comprehension.


# Example 1:
-------------------------

# Suppose we're given a list of names and we want to create a dictionary with the name of each student in the list as key, and 
# then a random score  (between 50 and 100) as the value, we can achieve that as follows:

import  random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {name:random.randint(50, 100) for name in names}

print(student_scores)           ---------------->          {'Alex': 86, 'Beth': 56, 'Caroline': 73, 'Dave': 62, 'Eleanor': 76, 'Freddie': 65}



# Example 2:
------------------------

# Suppose you're given a dictionary (called result_dict) of student names and their scores, and you're asked to use dictionary comprehension
# to create a new dictionary (called passed_students) of only those students with score of 65 and above.

result_dict = {'Alex': 86, 'Beth': 56, 'Caroline': 73, 'Dave': 62, 'Eleanor': 76, 'Freddie': 65}

passed_students = {name:result_dict[name] for name in result_dict if result_dict[name] >= 65}

print(passed_students)          ---------------->              {'Alex': 86, 'Caroline': 73, 'Eleanor': 76, 'Freddie': 65}


