# Reversing a list by slicing
# [::-1], step=-1
#   Copy a list
# [::], step=0 - start, stop, step

s = 'a00b00c00d'
# step(FIRST, spliting each iterable in groups, and picking the only the first char)
print(s[::3])

s = "Slicing is easy!"
s[2:14:3]
