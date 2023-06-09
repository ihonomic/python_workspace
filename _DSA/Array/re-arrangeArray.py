# Given an array, re-order so that element in even position is greater
# than the element before it and element in odd position are lesser
# than all elements before it.


def reOrder(arr):
    arr = [1, 2, 1, 4, 5, 6, 8, 8]
    """ 
    [ 1, 2, 1, 4, 5, 6, 8, 8 ] -> [4, 5, 2, 6, 1, 8, 1, 8]
    Clone array and sort it. 
    Cloning the array and sorting it, RETAINING the original indexes
    """
    arr2 = arr[:]
    arr2.sort()

    left, right = 0, len(arr)-1

    for i in range(len(arr)-1, -1, -1):        # loop from the end
        print(arr)
        if i % 2 != 0:                        # if odd, replace with the
            arr[i] = arr2[right]
            right -= 1
        else:
            arr[i] = arr2[left]
            left += 1

    return arr


# print(reOrder(arr))
# =============================================================
def reOrderArray(A):
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    """
    [-1,2,-3,4,5,6,-7,8,9] -> [4,-3,5,-1,6,-7,2,8,9]
    Re-order the array such that positive elements appears in odd positions 
    & negative elements in even positions
    """
    #   PARTITIONING
    # - QuickSort , consider 0 as pivot & divide the array around it
    #   Take all the negative to left side
    #   NOTE: the right side order isn't maintained.

    i = 0
    for j in range(len(arr)):
        if arr[j] < 0:
            # swap
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # [-1, -3, -7, 4, 5, 6, 2, 8, 9] -> The last negative number is before i, the first positive number will be at i
    negative, positive = 0, i

    while negative < positive and positive < len(arr):
        arr[negative], arr[positive] = arr[positive], arr[negative]

        negative += 2  # jump twice
        positive += 1  # jump once

    return arr


# print(reOrderArray([-1, 2, -3, 4, 5, 6, -7, 8, 9]))
# ======================= UNSOLVED ===========================================================


def reOrderArray2(A):
    """
    Re-order an array such that every positive number is followed by a negative number & vice versa. 
    Maintain the order of appearance 
    [1,2,3,-4,-1,4] -> [-4,1,-1,2,3,4]
    [-5,-2,5,2,4,7,1,8,0,-8] -> [-5,5,-2,2,-8,4,7,1,8,0]

    soln
    - Consider 'Out-of-place' elements, NOTE: negative elements should be in even indexes & positives in odd indexes
    - Swap if two opposite elements are out of place. 
    """
    arr = [1, 2, 3, -4, -1, 4]

    def rightRotate(array, outOfPlace, current):
        for i in range(i, outOfPlace, -1):
            array[i] = array[i-1]
        array[outOfPlace] = array[current]

    outOfPlace = -1
    for i in range(len(arr)):
        if outOfPlace >= 0:

            if (arr[i] >= 0 and arr[outOfPlace] < 0) or (arr[i] < 0 and arr[outOfPlace] >= 0):
                rightRotate(arr, outOfPlace, i)
            ...

        if outOfPlace == -1:
            ...

    print(arr)


# reOrderArray2([1, 2, 3, -4, -1, 4])
# ============================================

def moveZeros(A):
    """ 
    Move all zeros in the array to the end 
    """
    arr = [5, 0, 0, 4, 0, 3]

    i = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    return arr


# print(moveZeros([5, 0, 0, 4, 3]))
# =========================================================


def moveNegativePositives(A):
    """ 
    Move all negatives to left & positives to right, retaining the order
    - start from the second index
    - start from second index
    - if positive found, skip it,
    - if negative found, traverse it backwards until a negative is before it
    """
    # arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr = [5, 5, -3, 4, -8, 0, -7, 3, -9, -3, 9, -2, 1]

    for i in range(1, len(arr)):
        #   if element is positive, skip
        key = arr[i]
        if key > 0:
            continue

        #   if element is negative, shift all positive to the right
        #   previous index,
        j = i - 1
        # Stop if j is less than last index or a negative element is now prevoius
        while j >= 0 and arr[j] >= 0:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    return arr
# print(moveNegativePositives([12, 11, -13, -5, 6, -7, 5, -3, -6]))
