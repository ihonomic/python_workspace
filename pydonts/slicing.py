# Reversing a list by slicing
# [::-1], step=-1
#   Copy a list
# [::], step=0 - start, stop, step

s = 'a00b00c00d'
# step(FIRST, spliting each iterable in groups, and picking the only the first char)
# print(s[::3])

s = "Slicing is easy!"
s[2:14:3]

<<<<<<< HEAD
#   Negative steps - Like ranges, the start has to be larger than the stop, because it counts downwards

s = "Slicing is easy!".removeprefix("Slic")
=======
#   slice() method
#   __getitem__() is what performs slicing and indexes, behind the scene


def f(x): return x


s = "Slicing is easy!"
m = map(f, s)

print(list(m)[2::3])
>>>>>>> 0021d919c09f35cdcec4ade127846ed0b10d7380