# print the index and character in the string
for index, char in enumerate('Hellooooo'):
    print(index, char)

for index, char in enumerate([1,2,3,4,5]):
    print(index, char)

for index, num in enumerate(list(range(100))):
    if num == 50:
        print(f'Index of 50 is {index}')