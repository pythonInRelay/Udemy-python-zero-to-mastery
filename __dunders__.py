# This is just to give our program something to do
def print_hello():
  print("Hello")
  
# Prints the name of the main script running
# If the script isn't __main__ , it'll print the script name (without ".py")
# If it's the main script, it'll print __main__
print(__name__)

# Tells the program to only run this code if its being run from the main program
# and not from an imported program (so both progam's code isn't run on start)
if __name__ == '__main__':
  print_hello()