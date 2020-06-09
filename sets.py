# Same as dict, they are not ordered
my_set = {1, 2, 3, 4, 5, 5}
# Will not print the duplicate 5
print(my_set)

# Create a set of only unique values from a list
my_list = [1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9]
unique_set = set(my_list)
print(unique_set)

# Check if something is in the set
print(1 in my_set)

# Compare sets and show difference
print(my_set.difference(my_list))

# Intersection (or .intersection)
print(my_set & my_list)

# Union (or .union)
print(my_set | my_list)
