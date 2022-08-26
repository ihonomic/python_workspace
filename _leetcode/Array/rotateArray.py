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
    """ Look for the index of element where the previous element is greater than it  """
    left, right = 0, len(arr)-1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid-1] > arr[mid]:
            return mid

        if arr[mid+1] > arr[mid]:
            left = mid+1

    return left


# print(countRotation_BinarySearch([15, 18, 2, 3, 6, 12]))
