import random

# Methods are functions that belong to a class, which are used by the instance not the class
# Methods always take one parameter (which represents the instance using the method)
# All of the regular method rules apply, except the first argument ALWAYS has to be 'self'

class Thief:
    sneaky = True

    def __init__(self, name, sneaky = True, **kwargs):
    	self.name = name
    	self.sneaky = sneaky

    	# This means I could run e.g. daniel = Thief("Daniel", True, level=10, weapons=True) et cetera
    	# So I can now pass as many arguments as I like to be stored into a dictionary
    	for key, value in kwargs.items():
    		setattr(self, key, value)

    def pickpocket(self):
    	# We can call this in the REPL with e.g. daniel = Thief then daniel.pickpocket()
    	# If instance's sneaky attribute is set to true, try to pickpocket
    	return self.sneaky and bool(random.randint(0, 1))

        # We can call this below in the REPL with e.g. daniel = Thief() and then daniel.hide(4)
        # which will be also true, but only if sneaky is 1 from randint
    def hide(self, light_level):
    	return self.sneaky and light_level < 10


# Example 2

# class Student:
#     name = "Daniel"
    
#     def praise(self):
#         return f"You inspire me, {self.name}!"
    
#     def reassurance(self):
#         return f"Chin up, {self.name}. You'll get it next time!"
    
#     def feedback(self, grade):
#         if grade > 50:
#             return self.praise()
#         else:
#             return self.reassurance()

# Example 3

class RaceCar:
    color = 'blue'
    fuel_remaining = 10
    
    # We set the laps to 0 here because if we set it anywhere else all instances
    # would start with how many laps happened last time
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0
        
        for key, value in kwargs.items(): # Using kwargs here because we aren't
            setattr(self, key, value) # defining laps in the class but we still need laps
            
    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps += 1