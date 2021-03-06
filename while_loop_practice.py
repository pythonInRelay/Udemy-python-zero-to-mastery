# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75

# Solution 1 here
# Self explanatory, keep incrementally adding 25 until we reach 350

while current_oven_temp < 350:
    current_oven_temp += 25
    print(current_oven_temp)
else:
    print("The oven is ready!")

# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.

def total_and_average():
    numbers = []
    # Solution 2 here
    while True:
        num = input("""
        Please enter a number: 
        (Type 'q' to quit) """).lower()
    
        if num == 'q':
            break
            # Use a try block so we can catch an error (it's just good practice/habit)
        try:
            numbers.append(float(num))
        except ValueError:
            continue
    print("You entered: ", numbers,)
    print("The total is: ", sum(numbers))
    # This is an easy way to do an average, but there are other ways too (for ints/floats sum/len works fine)
    print("The average is: ", sum(numbers)/len(numbers))
    
total_and_average()

# Problem 3: Missbuzz
# Write a while loop that increments current by 1
# If the new number is divisible by 3, 5, or both,
# print out the number. Otherwise, skip it.
# Break out of the loop when current is equal to 101.

current = 1

# Solution 3 here

# Super easy, if the current number is under 101 keep adding 1
while current < 101:
    # Then print out if the number is divisible by 3, 5 or both
    if not current % 3 or 5 == 0:
        # Print the number if the above is True
        print(current)
    current += 1