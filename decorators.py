# Decorators: "Allows a function to borrow functionality from another function
# without needing to be re-written (keeping it DRY)"


def my_decorator(func):
    def wrap_func():
        print("""-- -- -- -- -- \n
        Printed from another function called 'my_decotrator()' \n
        hello() now also does this first!\n
        -- -- -- -- -- """)
        func()
        print("""-- -- -- -- -- \n This is also from the other function 'my_dectorator()' \n
        but hello()'s own function block runs before this bit! \n
        -- -- -- -- -- """)
    return wrap_func

# the @decotrator is the function whose code we want to include
# in our second function


@my_decorator
def hello():
    print('>>>>>>>>>> hello <<<<<<<<<<')


hello()


# What decorators are actually doing:

a = my_decorator(hello)
a()
