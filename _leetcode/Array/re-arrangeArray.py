# Given an array, re-order so that element in even position is greater
# than the element before it and element in odd position are lesser
# than all elements before it.

arr = [1, 2, 1, 4, 5, 6, 8, 8]


def reOrder(arr):
    """ 
    [ 1, 2, 1, 4, 5, 6, 8, 8 ] -> [4, 5, 2, 6, 1, 8, 1, 8]
    Clone array and sort it. 
    Cloning the array and sorting it, retaining the original indexes 
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


print(reOrder(arr))
