# Dictionary example
# Dictionaries are not ordered in the program's memory. Values can exist anywhere
# Dictionaries are good when you don't need to order the data, but you still want to be able to retreive the data with a specific variable name
# Dictionaries also hold more values
# Dictionary keys must be immutable (e.g strings, bool, tuple)

dictionary = {
    'a': [1, 2, 3],
    'b': 'word',
    'c': True,
}

# You can put dictionaries inside of lists
dict_list = [
    {
    'weapons': [1, 2, 3],
    'username': 'guest_user',
    'hasMagic': True,
    }
]

# Prints '2'
print(dict_list[0],[1])

# Print the 'key' value of 'b' which is 'word'
print(dictionary['b'])

# Test if this key is in the dictionary, returns True/False (and excepts errors)
print(dictionary.get('c'))
print('v' in dictionary)
print('c' in dictionary.values())
print('c' in dictionary.keys())
print('c' in dictionary.keys()) # Grabs from both keys and values

# This pushes a default/set value of e.g. 55 into the dict if none exists
print(dictionary.get('c', 55))

# Less common syntax example
user2 = dict(name = "username")
print(user2)

# Show all keys and values in a dictionary
dict_list.keys()
dict_list.values()
dict_list.items()

# Alphabatise keys
sorted(dict_list.keys())