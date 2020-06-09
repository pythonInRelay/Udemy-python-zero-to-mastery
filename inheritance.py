# Example of a parent class


class User():
    def __init__(self, email='@email.com'):
        self.email = email

    def sign_in(self):
        print("You're logged in!")

# Example of a child class


class Wizard(User):
    def __init__(self, name, power, email):
        # vv refers to the parent class, in this case User. Don't need to use 'self' here either.
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacked with a power of {self.power}.')


class Archer(User):
    def __init__(self, name='', remaining_arrows=100, arrows_used=0):
        self.name = name
        self.remaining_arrows = remaining_arrows
        self.arrows_used = int(input('How many arrows will you use? '))

    def attack(self):
        if self.arrows_used > self.remaining_arrows:
            print(
                f"You don't have enough arrows remaining! Arrows: {self.remaining_arrows}")
        else:
            self.remaining_arrows -= self.arrows_used
            print(
                f'Attacked with arrows. Arrows left = {self.remaining_arrows}.')


wizard1 = Wizard('Merlin', 50, 'something@mail.com')
archer1 = Archer('Robin', 100, 40)
print(wizard1.sign_in(), wizard1.attack(), archer1.attack())

# An example of Polymorphism
# Two different classes have the same function 'attack' but it does two different things


def player_attack(char):
    char.attack()


print(wizard1.email)
player_attack(wizard1)
player_attack(archer1)

# Check if instance (returns bool value)

print(isinstance(wizard1, Wizard))
