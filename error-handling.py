# Error handling

while True:
    try:
        age = int(input("What is your age? "))
        10 / age
    except ValueError:
        print("Please enter a number!")
    except ZeroDivisionError:
        print("Please enter a number that is not 0!")
    else:
        print("Thanks")
        break
    # finally runs ALWAYS at the end of the program when everything is done
    finally:
        print("Now we're done")

# Creating a function that includes error handling by default


def add_numbers(num1, num2):
    try:
        return num1 + num2
    # We're storing the error in the 'err' variable and then printing it for the user
    except (TypeError, ZeroDivisionError) as err:
        print(f"Please enter a number that isn't 0! {err}")


print(add_numbers(1, "2"))
