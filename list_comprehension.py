

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
