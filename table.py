travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

# This script shows how to basically make a table in python (without the physical table duh)

# Prints the FIRST list and SECOND item in that list
print(travel_expenses[0][1])

print("Travel expenses: ")
# Define which week (list) to start with
week_number = 1
# For each week (this is a new variable we will call later) do this with travel expenses list
for week in travel_expenses:
    # Printing the week with a bullet point and the cost spent each week using an in-built function "sum" (adding each list item together)
    print("* Week #{}: ${}".format(week_number, sum(week)))
    # Tell python to add 1 to each week number (because it's set to 1)
    week_number += 1