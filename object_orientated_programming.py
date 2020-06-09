# OOP
# Classes are essentially blueprints used to make objects


class NewObject:  # use a Capital starting and CamelCase
    pass


obj1 = NewObject()  # we're instanciating the class here
print(type(obj1))  # gives class __main__.NewObject

# Examples of Classes and Objects in use
# Adding an underscore before a variable tells other developers, do not modify this later
# Essentially it means the variable/method/etc is 'private


class PlayerCharacter:
    # Class Object Attribute
    membership = True  # not dynamic, static for all instantiated objects

    # This is a constructor function
    # __init__ instanciates the object
    def __init__(self, name='anonymous', age='0'):
        if (age > 18):
            self._name = name  # self signifies it's a dynamic attribute. We also need self, to tell each new instance to add this value to itself
            self._age = age  # these are attirbutes

    def whoami(self):
        print(f'My name is {self._name}')

    @classmethod  # this does not require instanciating e.g. player1 to be used
    def adding_things(cls, num1, num2):  # cls refers to 'class' like self refers to itself
        return num1 + num2

    # @staticmethod # exact same as classmethod except no access to 'cls'
    # use staticmethod when we don't care about modifying or using class attributess


player1 = PlayerCharacter('Daniel', 28)
print(player1.whoami())  # additional () needed to actually "run" the code
print(player1.adding_things(2, 3))
