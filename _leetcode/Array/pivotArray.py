# `===========================https://leetcode.com/problems/find-pivot-index/=========================================================


def pivotIndex(nums: list) -> int:
    """
    Search for the index where the sum(left) == sum(right)
    - Two pointers.
    - Let the right be the sum of the total array, 
    - Keep substracting from the right & adding to the left, if they become same
    - return the index

    """
    left, right = 0, sum(nums)
    for i, num in enumerate(nums):
        right -= num
        if left == right:
            return i
        left += num
    return -1
