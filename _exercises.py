def sort(l):
    m = min(l)
    idx = l.index(m)

    return [m] + sort(l[:idx]+l[idx+1:])


print(sort([9, 4, 4, 5, 7, 8, 1, 4]))
