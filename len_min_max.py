nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Len counts the link, so in this case it's 10 (the number of items in the list)
print(len(nums))
# Output: 10

# Min shows the lowest value integer or float in the list
print(min(nums))
# Output: 1

# Max shows the largest value integer or float in the list
print(max(nums))
# Output: 10

# For strings it's basically the same
# Len counts how many items are in the string
# Min will print the closest value to 'A' and Max the closest to 'Z'

# For mixed strings e.g. "string2019" python uses lexigraphical ordering
# Max would print out 't' and Min would print out '0'

# For strings with special characters e.g. "string2019!@#$%^&*()_+'"
string = "string2019!@#$%^&*()_+'"
# Python picks the "!" as the lowest value here
print(min(string))
# Max value is still "t"
print(max(string))