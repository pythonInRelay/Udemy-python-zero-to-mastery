# Fibonacci umbers using a generator


def fib(number):
    num1 = 0
    num2 = 1

    for i in range(number):
        # Produce num1 but don't store in memory
        yield num1
        # temporarily store num1 in memory to be added
        temp = num1
        num1 = num2
        num2 = temp + num2


for x in fib(20):
    print(x)


# Fibonnacci numbers using a list

def fib2(number):
    num1 = 0
    num2 = 1
    # Create an empty list
    result = []
    for i in range(number):
        # Add the first result to the list
        result.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2
    return result


print(fib2(20))
