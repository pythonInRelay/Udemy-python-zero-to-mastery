some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'f', 'f', 'f', 'g', 'h', 'i', 'j', 'k']

duplicates = []

# for each item in list
for item in some_list:
    # if it occurs more than once
    if some_list.count(item) > 1:
        # inform we have duplicates
        print('Yes this list has duplicates!')
        # adds the occuring duplicate only one time
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)

some_list = ['a', 'b', 'e', 'd', 'e', 'f', 'f', 'f', 'f', 'g', 'h', 'i', 'j', 'k']

# Crete an empty list to hold the following comprehension
duplicates = []

# For each item in some_list, add to duplicates if it occurs more than once
# Convert duplicates variable to set, to remove further duplicates
# Then convert to list
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)