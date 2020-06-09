# As soon as we return something from a function, the function block ends

def add_together(num1, num2):
    return num1 + num2

print(add_together(16,647))

# You can also define functions inside of other functions

def sum(num1, num2): # name = sum, 2 parameters take 2 arguments
    def second_function(n1, n2): # can only use this function inside the loop
        return n1 + n2
    return second_function # second_function did the arithmetic so return it
            # it also takes n1 & n1 and stores them in num1 & num2 for sum

total = sum(10, 20) # here we still call the original (highest) function
print(total(10, 20))