import contextlib
import os

#   Suppress an error - Alternative for Try and Except
#   The advantages of using with is that they close the file after use .
#   So if there'e no , __enter__, __exit__ dunder method for the object(context managers), it throws an attribute error
with contextlib.suppress(FileNotFoundError):
    os.remove('./jj.png')

#   SORTING
#   The key parameter in python functions(max, min, sorted, sort, ) takes a function attribute that is not
#   invoked but applies to all iterables
#   operator.itemgetter is a function that returns a function which, when invoked, will retrieve the item at specified index
import operator
mylist = [(3, 3, 1), (3, 2, 1), (1, 1, 1), (1, 3, 2), (2, 3, 2), (1, 2, 3)]


def by_3rdIndex(t):
    return t[2], t[1], t[0]


mylist.sort(key=operator.itemgetter(2, 1, 0))
#   Item getter can also take a slice s by invoking the slice() function
# Can also accept key and value names of a dictionary
