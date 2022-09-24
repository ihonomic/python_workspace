from functools import reduce
import operator


def _sum(iterE, start=0):
    acc = start
    for n in range(iterE):
        acc += n
    return acc


# print(reduce(_sum, range(10)))


def moveNegPos(A):

    for i in range(1, len(A)):
        key = A[i]

        if key > 0:
            continue

        j = i - 1
        while j >= 0 and A[j] > 0:
            A[j+1] = A[j]
            j = j - 1

        A[j+1] = key

    return A


print(moveNegPos([2, 3, -1, 4, -8]))
