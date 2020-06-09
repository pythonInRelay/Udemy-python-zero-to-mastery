# Generators
# "yield" turns a function into a generator
# and it is only used when defining a generator


def generator_func():
    for i in range(1000):
        #
        yield i


# Prints every single iteration of 'i' in range 1000

for item in generator_func():
    print(item)
