class TestClass:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        print('speak')


var1 = TestClass('Dan', 25)
var1._name = '!!!'
var1._speak = 'Uh oh'

print(var1.speak)
