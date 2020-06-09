# Filter "creates an iterator that will aggregate elements from two or more iterables"
# Like map, will not modify the original variable (in this case lists)

names = ['Dan', 'Mike', 'Sammy']
emails = ['dan@mail.com', 'mike@mail.com', 'sammy@mail.com']


print(list(zip(names, emails)))
