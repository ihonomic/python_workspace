import bisect
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


# print(moveNegPos([2, 3, -1, 4, -8]))


def reversePairs(nums: list) -> int:
    """ 
    Two conditions: 
        1) We can't reverse similar index, i.e when i == j, it must be compared when i < j
        2) ums[i] >  2 * nums[j] 
    Method 1: (time, space) = 0(n^2), 0(1):
            Quadratic Loop, comparing i & j 

    Method 2: (time, space) = 0(n), 0(n):


    """
    # count = 0
    # arr = []

    # for i in range(len(nums)):
    #     index = bisect.bisect_right(arr, 2*nums[i])
    #     count += len(arr) - index
    #     bisect.insort(arr, nums[i])
    #     print(f'{index=} {count=} {arr=}')

    # return count

    count = 0

    def merge(a, b):
        nonlocal count
        #   We just want to check if the nums at left is greater than twice of any at right, If yes, count
        left, right = 0, 0
        while left < len(a) and right < len(b):
            if a[left] > 2 * b[right]:
                count += len(a) - 1
                right += 1
            else:
                left += 1

        return sorted(a + b)  # help with sort

    def mergeSort(nums):
        if len(nums) <= 1:
            return nums

        #   get mid
        mid = len(nums) // 2

        #   sort left & right
        left = mergeSort(nums[:mid])
        right = mergeSort(nums[mid:])

        #   Merge left & left
        return merge(left, right)

    mergeSort(nums)
    return count


print(reversePairs([1, 3, 2, 3, 1]))
