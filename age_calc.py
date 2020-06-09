CURRENT_YEAR = 2019

# Step 1
# Ask the user for their name and the year they were born.

name = input("What is your name? ")
while True:
    birth_year = input("What year were you born? ")
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue
    else:
        break
# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.

age = CURRENT_YEAR - birth_year
turn_25 = (25 - age) + CURRENT_YEAR
turn_50 = (50 - age) + CURRENT_YEAR
turn_75 = (75 - age) + CURRENT_YEAR
turn_100 = (100 - age) + CURRENT_YEAR

# Step 3
# If they're already past any of these ages, skip them.

if turn_25 > CURRENT_YEAR:
    print("You'll turn 25 in the year {}, {}".format(turn_25, name))
if turn_50 > CURRENT_YEAR:
    print("You'll turn 50 in the year {}, {}".format(turn_50, name))
if turn_75 > CURRENT_YEAR:
    print("You'll turn 75 in the year {}, {}".format(turn_75, name))
if turn_100 > CURRENT_YEAR:
    print("You'll turn 100 in the year {}, {}".format(turn_100, name))