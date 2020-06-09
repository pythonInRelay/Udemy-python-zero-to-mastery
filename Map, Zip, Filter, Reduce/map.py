# Map "applies a function to all the items in an input_list"

# Map means we no longer need to e.g. create an empty list and write a 'for loop'
# All that's required is the mathematical formula
# Map also doesn't update any variable values in 2nd parameter

# Simple function with just the math formula


def multiply_by2(item):
    return item*2


# Tells us that it created an object to store in memory
# We also don't need to call the function with ()
print(map(multiply_by2, [1, 2, 3]))

print(list(map(multiply_by2, [1, 2, 3])))


# Example 2 (Work In Progress)

email_list = ['dan@mail.com', 'nam@mail.com',
              'sam@mail.com', 'dim@mail.com', 'kim@mail.com']


def remove_extension(com):
    return email_list.append('.com')


print(list(map(remove_extension, email_list)))
