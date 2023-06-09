from collections import Counter

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


# parity(5)
# ==========================================================================================
def checkCharacter(string1, string2):
    countOne = Counter(string1)
    countTwo = Counter(string2)

    mergeCount = countOne - countTwo
    print(mergeCount)
    count = 0
    for key, val in mergeCount.items():
        count += abs(val)

    print(count)


checkCharacter("bond", "down")
checkCharacter("aaaa", "bbbb")
checkCharacter("aabb", "baaa")
