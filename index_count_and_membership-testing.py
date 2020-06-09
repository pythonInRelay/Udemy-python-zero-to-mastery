docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

# The exact string below first appears at index 21 in docs
# NOTE: If the value is not found within the list/tuple/etc. it will return a ValueError
# This must be excepted otherwise the program will quit
print(docs.index('sequence'))
      
# The exact string below appears a total of 2 times in docs
print(docs.count('are'))

# "Membership Testing" means we are looking for the presence of something, in something else
# Usually depending on whether or not this is TRUE or FALSE, we opt to do something
if 'happy' in docs:
  print(f'We did find the word "happy" in the following: \n"{docs}"')
else:
    print(f'We did NOT find the word "happy" in the following: \n"{docs}"')


# concat adds 2 things together
# This is not memory efficient or fast, so consider doing something else if concatinating a lot of IMMUTEABLE variables

object1 = [1, 2, 3, 4, 5]
object2 = [6, 7, 8, 9, 10]

# Adds both the lists together, same thing will happen for tuple/string etc.
object3 = object1 + object2
print(object3)

# We can also use multiplication (division is unsupported for tuple)
object4 = object3 * 2
print(object4)