"""
Question: Create sub arrays from array
    arr = [3,1,2,4] -->
    [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]
"""


def subArrayFromArray(nums) -> list:
    array2D = []
    for i in range(len(nums) + 1):
        for j in range(i):
            array2D.append(nums[j:i])

    print(array2D)
    return array2D
