# So here we are making a new function
# The function is called add_two_numbers
# This function has two *parameters* called num1 & num2
# Parameters are not assigned a value until the function is called and an argument is passed
# Because these parameters take two arguments it MUST be passed 2 arguments ALWAYS
def add_two_numbers(num1, num2):
	# The above paremeters num1 and num2 are being stored in the new variable called val
	# We need to store the result of equation we make with num1 & num2 in val because we need to use val to update the value of the function add_two_numbers
	val = num1 + num2
	# When we use return, it updates the function add_two_numbers() with the sum of num1 & num2
	return val
	# Except that at this point in the program, add_two_numbers is empty >> we could see this if we wrote below print(add_two_numbers) << as it would just give us the memory address of the function
	# So all we've done is define the function and the two arguments we will pass it and what it will do with those and assign them in val which is only used to update the value of the function add_two_numbers
	# We haven't set the parameters num1 & num2 to anything (we do this below)

# Here we're printing out the value of add_two_numbers
# We're also passing the two required arguments which are 10 and 20
# We know that the function add_two_numbers will add them together as we defined
# So LITERALLY we are writing here print > DO add_two_numbers FUNCTION > USING 10 & 20 as arguments
print(add_two_numbers(10, 20))
# So what will be printed is:
# 30

# We can also add/subtract/multiply/append/join/etc strings, lists, basically anything.




# We could also do the above in a slightly different way that doesn't require making the variable val available only in the local context (as shown below)
# This might be a little better if we don't need/want the variable available only in the local context of add_two_numbers
def add_two_numbers(num1, num2):
	return num1 + num2
# This is another way to do this whilst making the function shorter, however we still need to store the answer in a variable
# We need to do this because the function add_two_numbers will be emptied after it runs
sum = add_two_numbers(6, 19)
# So what we just did was create the variable sum which will store the result of the add_two_numbers function
# We still haven't printed the result though, so let's do that
print(sum)
# The answer will be
# 25