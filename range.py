# start at 0, to 10 in steps of 2 at a time
for _ in range(0, 10, 2):
    print(_)

    # _ variable name tells any other developer we don't care
    # what the variable is and we won't use it

for __ in range(2):
    print(list(range(10)))

    # crates 2 lists using a range of 0 - 9