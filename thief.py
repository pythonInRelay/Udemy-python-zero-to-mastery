import random

# This is a 'parent' class to which other classes can inherit attributes
class Character:
	def __init__(self, name, **kwargs):
		self.name = name

		for key, value in kwargs.items():
			setattr(self, key, value)

# Thief is inheriting the init and dictionary (kwargs) attributes from character
class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
    	# When we use super() we have to include the method name and the required argument(s)
    	super().__init__(name, **kwargs)
    	self.sneaky = sneaky

    def pickpocket(self):
    	return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
    	return self.sneaky and light_level < 10