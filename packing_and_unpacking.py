# This is an example of packing
# Packing is perfect when we don't know how many parameters we need to specify

# Because this function has a multiplication sign at the beginning of the parameter
# It will store all of the arguments passed into a tuple
def packer(*args):
    print(args)
    
# In this case we're telling it to print the 4 arguments (which are strings) we're passing it
packer("Hello", "I", "love", "python")
# As this prints out a tuple the commas are shown in the print statement



# To iterate through each argument you can use a for loop
def packer(*args):
    for val in args:
        print(val)

# Now each string will be printed on its own line (and without a comma)
packer("Hello", "I", "love", "python")




######################
# UNPACKING
######################

# Opposite of packing
def unpacker():
    return (1, 2, 3)

# Pretty self-explanatory
# unpacker() is going to put the values 1, 2 & 3 into var1, var2 & var3
var1, var2,var3 = unpacker()
print(var1, var2, var3)

# You could also use a string like "hey" which will create h, e, y. 1 in each variable