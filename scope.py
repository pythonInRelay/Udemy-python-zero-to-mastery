# Scope = What variables des the program have access to?

a = 1 # This is in the global scope

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)

# Order
# 1 - Check if exists in local scope
# 2 - Check in parent local scope
# 3 - Check global (what is in no indentation)
# 4 - Check built in functions

# Force using global

nonlocal

total = 0

def counter():
    global total # first have to tell interpreter to use global total
    total += 1 # now we can use it
    return total

counter()
counter()
print(counter())