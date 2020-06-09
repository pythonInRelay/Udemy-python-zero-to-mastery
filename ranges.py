# Ranges take 3 parameters,
# Start, Stop and Step
# This means the range will start at 0, run 10 times and stop at 9 (not 10)
# If we leave out the Step variable it'll still pick 1 by default
for i in range(0, 10, 1):
  print(i)

# Python will always assume we're starting at 0 and iterating by 1 so this works more easily
# Here we're just specifing the stop value which is 10
for i in range(10):
  print(i)