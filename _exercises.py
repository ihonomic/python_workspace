from functools import reduce
import operator


def _sum(iterE, start=0):
    acc = start
    for n in range(iterE):
        acc += n
    return acc


print(reduce(_sum, range(10)))
