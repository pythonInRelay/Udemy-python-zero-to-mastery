# Sorts and reverses a list
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list1.sort()
# print(list1::-1) would also reverse the list, but creates a new version
list1.reverse()
print(list1)

# Makng lists using range (start, stop)
print(list(range(1, 100)))

# Join can add a value from another variable between each list item
separator = ', '
comma_separated_list = separator.join(['item1', 'item2', 'item3', 'item4'])
print(comma_separated_list)

# or, when we don't need to store the separator in its own variable
comma_separated_list = ', '.join(['item1', 'item2', 'item3', 'item4'])
print(comma_separated_list)

# Packing
a, b, c = [1, 2, 3]
print(a, b, c)

# Unpacking
