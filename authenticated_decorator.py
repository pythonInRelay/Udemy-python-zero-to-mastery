# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:

user_dict = {
    'name': 'Sorna',
    'has_access': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['has_access']:  # if the key 'has_access'
                                # in the dictionary is a Truthy value
            # return (in this case): message_friends(user_dict)
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user_dict)
