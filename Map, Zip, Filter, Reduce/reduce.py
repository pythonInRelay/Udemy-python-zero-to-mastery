# Reduce "applies a rolling computation to sequential pairs of values in a list"

from functools import reduce

names = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# accumulator becomes what ever the new int is from the list we're passing it
# does: 0 (accumulator) + 1 (list item) = 0 1
# next accumulator is now 1, so 1 (accumulator) + 2 (list item) = 1 2
# and so on...
print(reduce(accumulator, names, 0))
