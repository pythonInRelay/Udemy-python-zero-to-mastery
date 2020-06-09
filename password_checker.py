# Easy password to ****** length checker program

password = input('Please enter your password: ')
username = input('Please enter your username: ')
password_length = len(password)
hidden_password = ('*' * password_length)
special_characters = '!', '@', '#'

# Todo count and mention the amount of special characters, numbers, etc in password
# if special_characters in password == True:
#     print('Yes there are special characters in your password')

print(f'Hello, {username}. Your password {hidden_password} is {password_length} characters long.')
# print(special_characters)