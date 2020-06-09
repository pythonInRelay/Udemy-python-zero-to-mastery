# Create a new empty list named shopping list
shopping_list = []
# price_list = []
    
#def add_price(price):
#    price_list.append(price)
#    float(price)

# Next define all of the functions we are going to use for this program
def show_help():
    print("What should we add to the shopping list? ")
    print ("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' to get help.
    Enter 'SHOW' to show the list.
    """)
    
    
def add_to_list(item):
    shopping_list.append(item)
    # Notify the user how many items are in the list
    print("You have {} items in the shopping list!".format(len(shopping_list)))
    
    
def show_list():
    print("Here is your list: ")
    for item in shopping_list:
        print(item)
 
show_help()

# This creates an endless loop because True will always be True
# Another way to do this would be e.g.:
# while program = True      >> and then at the end when DONE is entered change program to False
while True:
    # Specifies a blank input for the user to add items
    new_item = input("> ")
    if new_item == 'DONE':
        # Exists the outermost loop cleanly if the user types DONE (in all CAPS)
        break
        # Make the rest of the functions available if the user hasn't typed DONE
    elif new_item == 'HELP':
        show_help()
        # We're using elif so a conintue is needed after each function to stay in the loop
        continue
    elif new_item == 'SHOW':
        show_list()
# Sends the program back to the start of the while loop above ^^^ (must be part of the while block)
        continue
          

# Call add_to_list (it must be part of the above block (aka indented!) otherwise it runs separately and only adds the last thing written to the list before the while loop is ended, which in this case is DONE
    add_to_list(new_item)

# Call add_price
# add_price(item_price)

# Show the list at the end (remember that DONE doesn't show the list, it just stops the while loop, so we still need to show the list at the end
show_list()