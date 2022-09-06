# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(arr):
    """
    return Count the total elements left after a quantity of duplicates have been removed.
    E.g - You can be asked to leave maximum of 2 duplicates Only
    NOTE: elements at the end still exist but the program wants only the count
    """

    # if 2 duplicates is allowed
    k = 0

    for n in arr:
        if k < 2 or arr[k-2] != n:
            arr[k] = n
            k += 1
    return k

    #  if 1 duplicate is allowed
    k < 1 or arr[k-1]
