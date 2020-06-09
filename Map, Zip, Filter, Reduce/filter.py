# Filter "creates a list of elements for which a function returns true"
# Like map, will not modify the original variable

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
