# List Comprehensions

#   Plainly it's: variable_name(plus expression)
#       -> for(loop) variable name in string/range/list/etc.
#            -> if(conditional expression)

my_list = [char for char in 'hello']
my_list2 = [num*2 for num in range(0, 100)]

# multiply each list number in range 0-99 and show only even numbers
my_list3 = [num*2 for num in range(0, 100) if num % 2 == 0]
print(my_list, my_list2, my_list3)

# Set Comprehensions (Sets do not allow duplicates)
# Same shit but just change brackets to curly braces

my_set = {char for char in 'hello'}
print(my_set)

# Dictionary Comphrehensions

example_dict = {
    'a': 1,
    'b': 2
}
# what we want to do with data -> method for doing (for loop) -> using this data
my_dict = {key: value**2 for key, value in example_dict.items()}
print(my_dict)

# key and value are numbers from the below lists
my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)

dupes_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Converting the list to set removes duplicates from the print out
# otherwise we get b, b, n, n etc.

# x is a common variable name
# Literally written:
# variable dupes equals ->
#   variable name, AND for that variable in dupes list ->
#       if it appears more than once
#           add it to the dupes list
#               print the set and then turn that back into a list

# Need to read from right to left to make better sense
dupes = list(set([x for x in dupes_list if dupes_list.count(x) > 1]))
print(dupes)
