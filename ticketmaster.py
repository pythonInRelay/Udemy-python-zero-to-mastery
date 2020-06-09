TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining:
    user = input("Welcome to the ticket machine, please write your name? ")
    print("Hello, {}!".format(user))
    print("There are currently {} tickets remaining!".format(tickets_remaining))
    mytickets = int(input("How many tickets would you like to purchase {}?\n(They are $10 each and {} tickets remain): ".format(user, tickets_remaining)))
    try:
        mytickets = int(mytickets)
        if mytickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining!".format(tickets_remaining))
    except ValueError as err:
        print("Ran into an error. {} Please enter a valid answer next time.".format(err))
    else:
        total = calculate_price(mytickets)
        print("Your total is ${}, which includes a $2 service charge.".format(total))
        confirmation = input("Please confirm your purchase.\n(Enter Y/N): ")
        if confirmation.lower() == "y":
            print("Thanks for your purchase!")
            tickets_remaining -= mytickets
        else:
            print("Ok {}, your purchase was cancelled. You have not been charged.".format(user))
    print("There are still {} tickets remaining.".format(tickets_remaining))
print("Sorry there are no tickets left!")