# Classes

# Classes do not "run"

# Class names start with a capital letter
class Thief:
    sneaky = True

    def pickpocket(self):
        return bool(random.randint(0, 1))

# Importing a class
from filename import Classname

# Set a variable to a class
daniel = Thief()
print(daniel.sneaky)

# Check the value of attributes in a class
Thief.sneaky
daniel.sneaky

# Change the value in the active instance (doesn't change the class)
daniel.sneaky = False