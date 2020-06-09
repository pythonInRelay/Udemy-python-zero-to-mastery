def highest_even(list):
    evens = [] # make a list to store evens in
    for value in list:
        if value % 2 == 0: # if when dividing by 2 there is no remainder
            evens.append(value) # add the even value to the evens list
    return max(evens) # use max to return highest even

print(highest_even([10, 2, 3, 4, 5, 11]))