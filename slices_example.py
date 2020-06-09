nums = [1, 2, 3, 4, 5, 6, 7, 8]
# The below tells Python to start from 0, all the way to the end, but in steps of 2
# A step value of -1 makes the slice go backwards 1 at a time (-2, 2 at a time etc).
nums_partial = nums[::-1]
print(nums_partial)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# This means print from index 4 to 5 (it doesn't include the last index listed)
colors_partial = colors[3:6]
print(colors_partial)
# Output will be:
# 'green', 'blue', 'indigo'