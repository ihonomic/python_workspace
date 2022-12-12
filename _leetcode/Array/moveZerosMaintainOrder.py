"""
Question: Move zeros
    While maintaining the order of an array, move all zeros to the end.
    [1,0,5,5,0,0,0,3] --> [1,5,5,3,0,0,0,0]
    - Record the position of zero, and only swap if the current number is not zero
"""


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

