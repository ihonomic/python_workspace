# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(arr):
    """ Count the total elements left after a quantity of duplicates have been removed.
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
    # k < 1 or arr[k-1]


def removeDuplicates2(nums) -> int:
    """ 
    Method 1
        - Start replacing current index element with the last 2 previous
    Method 2
        Remove duplicates and leave at most 2 occurrences
        - Since the elements are sorted, replace third occurrences with '_' 
        - Shift all _ to the end
        - pop _
    """
    k = 0

    for n in nums:
        if k < 2 or nums[k-2] != n:
            nums[k] = n
            k += 1
    return k

    #   Method 2
    value = float("inf")
    count = 0

    for j, n in enumerate(nums):
        if n == value and count == 2:
            nums[j] = "_"
        elif n == value and count < 2:
            count += 1
        else:
            value = n
            count = 1

    #   shift the undergoes to the end
    #   find underscore? Replace with the next real number

    for i in range(len(nums)):
        if nums[i] == "_":
            for j in range(i+1, len(nums)):
                if nums[j] != "_":
                    nums[j], nums[i] = nums[i], nums[j]
                    break

    #   Remove the set of last underscores
    _count = nums.count("_")
    for _ in range(_count):
        nums.pop()
