# *args accepts any number of arguments
# **kwargs accepts any number of keyword arguments


def super_func(*args, **kwargs):  # kwargs will make a dict
    total = 0
    for items in kwargs.value():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=2, num2=10))

# Rules: params, *args, default params, **kwargs