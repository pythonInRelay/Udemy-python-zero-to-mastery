# A statement is an entire LINE code
# An expression is something that returns value (e.g. name / age)

# Escape sequence = everything after the \ is treated as a string
# \n = new line
# \t = add a tab before this

# Python 2 formatted strings
age = 12
name = 'Dan'
print('Hi {1}. You are {0} years old'.format(age, name))
# This prints the name and age backwards because in the {} we are specifcing the order
# It's better to use f-Strings

# List gotchas

selfish = 'me me me'
print(selfish[0],[2],[5])
# prints m [2] [3]
print(selfish[0 + 3 + 1])
# prints the 4th e

greet = 'helloooooo'
print(greet[0:len(greet)])
# prints start, to the length of greet (which is 10) a.k.a the whole of greet