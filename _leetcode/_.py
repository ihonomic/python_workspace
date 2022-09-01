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
#   Method 1
def commonChars(arr):
    check = list(arr[0])
    for word in arr[1:]:
        repatedChar = []
        for char in word:
            if char in check:
                repatedChar.append(char)
                check.remove(char)

        check = repatedChar
    return check

#   Method 2


def commonChars2(arr):

    res = Counter(arr[0])

    for word in arr[1:]:
        res &= Counter(word)

    return list(res.elements())


print(commonChars2(["bella", "label", "roller"]))
