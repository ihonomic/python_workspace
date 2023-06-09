""" Question 1 - Binary search
    Write a func that takes a sorted array & a target and then return the index of the target if its in the array
    otherwise return -1
    e.g : array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=33 --> 3
    METHOD: 0(logn) time | 0(1) space
"""


def binarySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            left += 1
        else:
            right -= 1

    return -1


""" Question 2 - Find 3 largest Number 
    Write a func that takes in an array & return the three largest number in an array.  Don't use sort()
    e.g : array=[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7] --> [18, 141, 541]
    METHOD: 0(n) time | 0(n) space
        Initialize to negative infinity, During the loop, shift values and update
"""


def findThreeLargestNumbers(array):
    threeLargest = [float("-inf")] * 3
    for num in array:
        if num > threeLargest[2]:
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = threeLargest[2]
            threeLargest[2] = num
        elif num > threeLargest[1]:
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = num
        elif num > threeLargest[0]:
            threeLargest[0] = num

    return threeLargest


""" Question 3 - Search in a sorted Matrix 
    Given a two dimensional matrix, each row and column is sorted (distinct integers) and a target. 
    The matrix doesn't necessary have the same height and width. Return the index of the target row & col
    if target not in matrix, return [-1, -1]
    e.g : matrix=[
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ] target=44 --> [3, 3]
    METHOD 1: 0(n * m) time | 0(1) space
    METHOD 2 : 0(n +m) time | 0(1) space
"""


def searchInSortedMatrix(matrix, target):
    # 0(n * m) time | 0(1) space
    for idx, row in enumerate(matrix):
        if target in row:
            return [idx, row.index(target)]
    return [-1, -1]


def searchInSortedMatrix(matrix, target):
    # 0(n +m) time | 0(1) space
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]


"""Question - Shifted Binary Search - Find the minimum element
    Write a func that takes in a rotated sorted array and return the minimum element
    e.g : nums=[45, 61, 71, 72, 73, 0, 1, 21, 33, 37]   --> 0
    METHOD: 0(logn) time | 0(1) space
    - If the mid element, is greater than the right element, that's abnormal, shift the left pointer after mid 
    - if the mid element is less than the  right element, that's normal, shift the right pointer to mid
    - If its equal, reduce right pointer by 1
"""


def findMin(nums) -> int:
    leftIdx = 0
    rightIdx = len(nums) - 1
    while leftIdx < rightIdx:
        mid = leftIdx + (rightIdx - leftIdx) // 2
        if nums[mid] > nums[rightIdx]:
            leftIdx = mid + 1
        elif nums[mid] < nums[rightIdx]:
            rightIdx = mid
        else:
            rightIdx -= 1

    return nums[leftIdx]


"""Question 4 - Shifted Binary Search 
    Write a func that takes in a rotated sorted array and a target and return the 
    index of the target if found, otherwise return -1 
    e.g : array=[45, 61, 71, 72, 73, 0, 1, 21, 33, 37] target=33  --> 8
    METHOD: 0(logn) time | 0(1) space
"""


def shiftedBinarySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:

        #   Does it contain duplicates(Don't do this if DISTINCT)
        while left < right and array[left] == array[left + 1]:
            left += 1
        while left < right and array[right] == array[right - 1]:
            right -= 1

        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid

        if array[left] <= array[mid]:
            # Does the target fall within the bounds
            if array[left] <= target <= array[mid]:
                right -= 1
            else:
                left += 1
        else:
            if array[mid] <= target <= array[right]:
                left += 1
            else:
                right -= 1
    return -1


""" Question 5 - Search for range 
    Write a func that accepts a sorted array and a target, and return the start and end index in an array but if target
    doesn't exist in the array return [-1, -1] 
    e.g : array=[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73] target=45 --> [4, 9]
    METHOD: 0(logn) | 0(1)
        # Look for a number larger than the target. so that the found number will be  -1 away from the actual target
"""


def searchForRange(array, target):
    start = search(array, target)
    end = search(array, target + 1) - 1

    if start <= end:
        return [start, end]
    return [-1, -1]


def search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target <= array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


""" Question 6 - Quick Select 
    Write a func that takes an array of integers and return the kth smallest in the array
    e.g : array=[8,5,2,9,7,6,3], k =3 --> 5
    METHOD 1: 0(nlogn) time | 0(1) space
    METHOD 2:  Quick-Sort technique: 0(n) time | 0(1) space
    - We're looking for the kth element from the end. 
    - The idea is to make a pivot index equal to the kth element 
    - First pivot element will start at 0
"""


def quickselect(array, k):
    #  0(nlogn) time | 0(1) space
    k = k % len(array)
    array.sort()
    return array[k - 1]


def quickselect(array, k):
    k = len(array) - k
    return quickSelectHelper(0, len(array) - 1, array, k)


def quickSelectHelper(startIdx, endIdx, array, k):
    pivotIdx = startIdx
    for idx in range(startIdx, endIdx):
        # Use <: if you're looking for kth largest
        if array[idx] > array[endIdx]:
            swap(idx, pivotIdx, array)
            pivotIdx += 1
    swap(pivotIdx, endIdx, array)

    # Decide which direction to go
    if pivotIdx > k:
        return quickSelectHelper(startIdx, pivotIdx - 1, array, k)
    elif pivotIdx < k:
        return quickSelectHelper(pivotIdx + 1, endIdx, array, k)
    else:
        return array[pivotIdx]


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


""" Question 7 - Index equals value 
    Write a func that takes in a sorted array and return the first element that equals it's index
    e.g : array=[-5, -3, 0, 3, 4, 5, 9] --> 3
    METHOD 1:  0(n) time | 0(1) space
    METHOD 2: 0(logn) time | 0(1) space
"""


def indexEqualsValue(array):
    # 0(n) time | 0(1) space
    for idx, num in enumerate(array):
        if num == idx:
            return idx
    return -1


def indexEqualsValue(array):
    # 0(logn) time | 0(1) space
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == mid and mid == 0:
            return mid
        if array[mid] == mid and array[mid - 1] < mid - 1:  # why?
            return mid

        if array[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1
