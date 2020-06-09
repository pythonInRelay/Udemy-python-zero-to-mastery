# Steps to super clean code

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

print(is_even(50))

# We're just checking for truthiness of even numer or not so
# Can be shortened to

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# But we actually don't need the elif at all

def is_even(num):
    if num % 2 == 0:
        return True

# In fact we don't even need the 'return True' line
# Python will return True/False already on a statement like this

def is_even(num):
    return num % 2 == 0

# Now we can just run ... to get our answer

print(is_even(56))