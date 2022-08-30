A = [1, 3, 2, 1, 4, 17, 9]


def even_odd(A):
    next_even, next_odd = 0, len(A) - 1

    while next_even <= next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

#   Parity


def parity(x):
    result = 0
    while x:
        result = result ^ x & 1
        x >>= 1  # reduce the input
    return result


parity(5)
