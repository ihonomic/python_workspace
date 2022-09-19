""" Decorators wrapps your function and modify the behaviour. """
"""A decorator is just a function that receives a function argument and returns a function argument:"""


# 1. A debugger -  Decorator that prints the arguments and return value

def print_debugger(f):
    def new_function(*args, **kwargs):
        print(
            f"Inside print debugger with {f.__name__}. with {args = } and {kwargs = } ")

        res = f(*args, **kwargs)

        print("Done.")

        return res

    return new_function


@print_debugger
def say_hi():
    print("Hi")


@print_debugger
def add(a, b):
    return a + b


# say_hi()
add(3, 4)
