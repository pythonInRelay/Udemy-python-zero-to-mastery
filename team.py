# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
add_players = input("Would you like to add a player to the list? ")

while add_players.lower() == "yes":
    name = input("\nPlease enter the player's name ")
    players.append(name)
    add_players = input("Would you like to add another player? (Yes/No) ")

# TODO print the number of players on the team
print("\nThere are {} players on the team".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
# This line means that for every player in "players" entered into the list, add 1 to their number starting with 1
for player in players:
    print("Player {}: {}".format(player_number, player))
    player_number += 1

# TODO Select a goalkeeper from the above roster
keeper = input("Please select a goal keeper by selecting the player number. (1-{})".format(len(players)))

keeper = int(keeper)

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Cool! The goalkeeper for the game will be {}".format(players[keeper - 1]))