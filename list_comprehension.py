
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
