# This is what Generators actually do


class MyGen():
    # The starting STATE for the generator is set to 0
    current = 0
    # Below defines the arguments that MyGen will take aka (itself, first num, last num)

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Create an iterable
    def __iter__(self):
        return self

    # Calling a next function

    def __next__(self):
        # If the current STATE is greater than the last STATE (which is always) then += 1
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        # When current is no longer less than last, raise to stop
        raise StopIteration


# Make a new variable called gen which equals the class MyGen
# Pass it two numbers we defined in the class (first, last)
# For each iteration (called 'i') print the value of 'i'.
gen = MyGen(0, 100)
for i in gen:
    print(i)


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator)
#         except StopIteration:
#             break


# special_for([1, 2, 3])
