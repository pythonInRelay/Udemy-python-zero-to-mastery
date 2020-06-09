# Find duplicates in a list

some_list = ['a','b','c','b','d','m','n','n']

# Make empty list to store duplicates
duplicates = []

for value in some_list:
   if some_list.count(value) > 1: # count check how many times the value appears, in this case we append if it's larger than 1 (once)
        if value not in duplicates: # TRICKY but cnow heck the dupes list and only print the items duplicate items ONCE
            duplicates.append(value) # append that value to the empty dupes list

print(duplicates)