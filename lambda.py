# Lambda "one time use expressions"

my_list = [1, 2, 3]

print(list(map(lambda item: item * 5, my_list)))

# Squared list exercise

square_list = [5, 4, 3]

print(list(map(lambda num: num ** 2, my_list)))


# Sorting
# Sort by the second number and from lowest value (i.e. -1)
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# Method 1
print(sorted(a, key=lambda x: x[1]))

# Method 2
a.sort(key=lambda x: x[1])  # Lambda typically uses 'x' as the variable name
print(a)
