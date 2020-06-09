groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']
# For each string in the above list groceries
# Add a value in the variable we call index before value of the variable item
# Enumerate (built-in function) will be used to number each following variable value
for index, item in enumerate(groceries, 1): # The number enumerate starts with is 0, but it takes a second argument which we can use to pick the number, in this case 1
  # “formatted string literals,” f-strings are string literals that have an f at the beginning
  # and curly braces containing expressions that will be replaced with their corresponding values
  # in this case the index and item (we could leave the {} blank but then it's less readable)
    print(f'{index}. {item}')



    # Another example
 def to_lowercase(input):
     return input.lower()

name = "Eric Idle"
f"{to_lowercase(name)} is funny."

# Prints
# 'eric idle is funny.'


# Multiline f-String

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
	f"Hi {name}. "
	f"You are a {profession}. "
	f"You were in {affiliation}."
)
message
# Prints (and we didn't even need to use the print statement)
# 'Hi Eric. You are a comedian. You were in Monty Python.'