from collections import deque
import math

#   ======================== NUMBER 1 - REVERSING ARRAY - =====================
# EXPECTED RESULT => [3 4 5 6 7 1 2 ]
#  (time, space) complexity = 0(n), 0(1)

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

#   METHOD 1 - Reversal Algorithm


def rotateArray(arr, d, n):
    """
    # -  Reverse range d
     [1, 2, |    3, 4, 5, 6, 7]

    # -   Reverse range n-d

    # -   Reverse full n
    """

    def reverseRange(arr, start, stop):
        while start < stop:
            #   Swap
            arr[start], arr[stop] = arr[stop], arr[start]

            start += 1
            stop -= 1

    d = d % n

    reverseRange(arr, 0, d-1)
    reverseRange(arr, d, n-1)
    reverseRange(arr, 0, n-1)

#   METHOD 2


def traverseArray(arr, d, n):
    start = 0
    while start < d:
        for i in range(n-1):
            arr[i], arr[i+1] = arr[i+1], arr[i]
        start += 1


# rotateArray(arr, d, n)
# traverseArray(arr, d, n)

# ======================== RIGHT ROTATING AN ARRAY =========================================
def rightRotateByK(arr, k):
    """
    Rotate the array by k element from the right, e.g k=3 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    Method 1
            - 0(n^2) TC swaps, starting from the end
    Method 2 
            - Limit k, k % len(arr) - incase k greater than the length
            - Rotate k length,
            - Rotate arr - k length
            - Rotate arr
    """

    k = k % len(arr)

    #  METHOD 1
    # for j in range(k):
    #     for i in range(len(arr)-2, -1, -1):
    #         arr[i], arr[i+1] = arr[i+1], arr[i]

    #   METHOD 2

    #   REVERSE ALGORITHM - (time, space) complexity = 0(n), 0(1)

    # 1, 2, 3, 4, 5, 6, 7, 10, 9, 8 - rotate k
    # 7,6,5,4,3,2,1 10, 9, 8 - rotate n-k
    # 8,9,10,1,2,3,4,5,6,7 - rotate n

    first, last = 0, len(arr)-1

    rotateLength(arr, len(arr)-k, last)
    rotateLength(arr, first, last-k)
    rotateLength(arr, first, last)

    def rotateLength(self, arr, start, stop):
        while start < stop:
            arr[start], arr[stop] = arr[stop], arr[start]
            start += 1
            stop -= 1


print(rightRotateByK([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


# =====================  NUMBER 2 - ROTATE ARRAY (CYCLIC) ABOUT FIXED POINT =============================

# EXPECTED RESULT => [7, 1, 2, 3, 4, 5, 6]
#  (time, space) complexity = 0(n), 0(1)
arrCycle = [1, 2, 3, 4, 5, 6, 7]

#   METHOD 1 - Slicing


def cyclicArray(arr):
    return arr[-1:] + arr[:-1]  # Assume about the last Index

#   METHOD 2


def reversalAlgo(arr):
    start, stop = 0, len(arr) - 1
    while start <= stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
    return arr

#   METHOD 3
# collections.deque(arr).rotate(-1)


# print(cyclicArray(arrCycle))
# print(reversalAlgo(arrCycle))

# ========================= ROTATING ARRAY USING deque().rotate() ====================================================================


def maximumSum(arr):
    array = deque(arr)
    sums = 0

    for _ in range(1, len(arr)):
        # rotate the array leftward
        array.rotate(-1)

        calc = sum([index * num for index, num in enumerate(array)])

        if calc > sums:
            sums = calc

    return sums


# print(maximumSum([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# ===============================================================================================================================
#   METHOD 1
def countRotation(arr):
    """ 
    1. This counts the number of times the array was rotated left-ward before it was sorted 
    2. Linear Search, find the index of the minimum element
    3. Binary Search, Find the index of the element where the previous element is greater than it
    """
    array = deque(arr)

    #   Auxillary Function
    def isSorted(arr):
        for i in range(n-2):
            if arr[i] > arr[i+1]:
                return False
        return True

    count = 0

    while True:
        if isSorted(array):
            break
        else:
            array.rotate(-1)
            count += 1
    return count

#   METHOD 2 - Binary search


def countRotation_BinarySearch(arr):
    """ 
    - Look for the index of element where the previous element is greater than it 
    - Minimum element
    """
    left, right = 0, len(arr)-1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid-1] > arr[mid]:
            return mid

        if arr[mid+1] > arr[mid]:
            left = mid+1

    return left


# print(countRotation_BinarySearch([15, 18, 2, 3, 6, 12]))

# ========================== FIND INDEX OF A TARGET IN A ROTATED ARRAY  =================================================================
def search(nums, target):
    """ 
    Search for the new index of a number in an already rotated sorted array. 0(logn)
    - min(), max() - If no target is given, but you're required to find the minimum or maximum index
    - if numbers are not distinct perform a while loop to eliminate repeated numbers. 
    """
    left, right = 0, len(nums) - 1
    while left <= right:

        # ==========================
        #   Does it contain duplicates(Don't do this if DISTINCT)
        while left < right and nums[left] == nums[left+1]:
            left = left+1
        while left < right and nums[right] == nums[right-1]:
            right = right - 1
        # ==============================

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        #   Since only one side can be sorted from the middle
        #   Is it left? - Compare left element to mid
        if nums[left] <= nums[mid]:
            #   Check if the target falls in-between left side
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Is right?
            #   Check if the target falls in-between right side
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# print(search([4, 5, 6, 7, 0, 1, 2], 0))

# =========== FIND THE START AND END INDEX OF A TARGET 0(logn) ==========================
def searchRange(self, nums: list, target: int) -> list:
    """
        - starting & ending position of a target.  
        - Binary search the target. 
        - Binary search the number greater than the target. Since array is sorted.
        - E.g => [1,2,3,7,7,7,7,8,10]
    """

    def search(x):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2

            if x <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    start = search(target)

    # Find index of the num greater than the target, substract by 1,
    #  to get the previous index that is similar to the target.
    end = search(target+1) - 1

    if start <= end:
        return [start, end]

    return [-1, -1]
