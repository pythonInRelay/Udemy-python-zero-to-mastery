# Functions

# Default Parameters
def say_hello(name='Darth Vader', age=66):
    print(f'Ayy lmao {name} {age}')

# Positional arguments
say_hello('Dan', 45)
say_hello('Tom', 19)

# Keyword arguments
say_hello(name='Ya mum', age=45)

# Show default
say_hello()

# 1 defined, 1 default
say_hello('Mike')