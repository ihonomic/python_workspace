<<<<<<< HEAD
from functools import reduce
import operator


def _sum(iterE, start=0):
    acc = start
    for n in range(iterE):
        acc += n
    return acc


print(reduce(_sum, range(10)))
=======
>>>>>>> 0021d919c09f35cdcec4ade127846ed0b10d7380
