""" Question: Permutation

    METHOD: 0(n*n!) time | 0(n*n!) time
"""


def getPermutations(array):
    result = []

    if len(array) == 1:
        return [array.copy()]  # form a new array and don't modify the main array

    for _ in range(len(array)):
        # remove one element, recursively
        n = array.pop(0)
        perms = getPermutations(array)

        # add the removed element to each permutations
        for perm in perms:
            perm.append(n)
            result.append(perm)  # TAKE NOTE: if the question demands it to be unique, check if a similar perm is not
            # already in result before add it

        # add the removed element to the end, for the next permutations
        array.append(n)
    return result

