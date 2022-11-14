"""  Question 1 : Bubble Sort
    METHOD :
        BEST CASE: 0(n) time | 0(1) space,
        AVERAGE CASE: 0(n^2) time | 0(1) space
        WORST CASE: 0(n^2) time | 0(1) space
    Two loops, set a flag, and return immediately there isn't swap
"""


def bubbleSort(array):

    for i in range(len(array)):
        swapped = False

        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                swapped = True

        if not swapped:
            return array
    return array


"""  Question 2 : Insertion Sort
    METHOD : 0(n^2) time | 0(1) space
    Start from the second index, compare element with the previous,
    Continue to swap previous and next previous. 
"""


def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


"""  Question 3 : Selection Sort
    METHOD :  0(n^2) time | 0(1) space
    Selection sort, is to contineously find the minimum element from the 
    right side and replace with current index.
"""


def selectionSort(array):

    for i in range(len(array) - 1):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        swap(i, minIdx, array)
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


"""  Question 4 : Three Number sort
    Given an array and an order which is a 3-distinct array of integers, sort the array base on the order
    e.g: array=[1,0,0,-1,-1,0,1,1] order=[0,1,-1] --> [0,0,0,1,1,1,-1,-1]
    METHOD : 0(n) time | 0(1) space
        # since order size is always 3.
        # consider swapping for only the first & second order, so that the left-over 
        # elements is assumed to belong to the third order
"""


def threeNumberSort(array, order):
    currIdx = 0
    for i in range(2):
        # since order size is always 3.
        # consider swapping for only the first & second order, so that the left-over
        # elements is assumed to belong to the third order
        value = order[i]
        for j in range(currIdx, len(array)):
            if array[j] == value:
                array[j], array[currIdx] = array[currIdx], array[j]
                currIdx += 1
    return array


""" Question 5: Quick sort
    View animation : https://yongdanielliang.github.io/animation/web/QuickSortNew.html
    Method : 0(nlogn) time | 0(logn) space - Average
        - swap if element at the left is greater than pivot, and right is less than pivot
        - swap right and pivot when right move past left
        - Recursively sort the left & right side subarray (right idx is the mid-way point)
"""


def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while rightIdx >= leftIdx:
        # array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]
        if array[leftIdx] > array[pivotIdx] > array[rightIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    #  swap
    swap(pivotIdx, rightIdx, array)

    # sort the resulting subarrays but consider the smaller one first
    #         R
    # [5,5,|2|,3,6,8,9]
    quickSortHelper(array, startIdx, rightIdx - 1)
    quickSortHelper(array, rightIdx + 1, endIdx)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


""" Question 6: Heap sort
    Method : 0(nlogn) time | 0(1) space
        # Begin by building a max heap. 
        # Remember that the root value in a max-heap is the largest
    
        # Contineously Swap with first and the last indexes of the left sub-arrays
        # siftdown by moving its new value to its right position. i.e comparing 2 child node downwards
        # This will result in the root node having the next greatest value 
"""


def heapSort(array):
    # 0(nlogn) time | 0(1) space

    # Begin by building a max heap.
    # Remember that the root value in a max-heap is the largest

    # Contineously Swap with first and the last indexes of the left sub-arrays
    # siftdown by moving its new value to it right position.
    # This will result in the root node having the next greatest value

    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)  # before the endIdx
    return array


def buildMaxHeap(array):
    # Find the first parent node index by considering the last one, that is not a leaf & then reverse
    firstParentIdx = (len(array) - 1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)


def siftDown(currentIdx, endIdx, heap):
    # Get the two children nodes
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        # which of the children nodes will be swapped
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        # Should we swap ? Or is the current reach it's rightful position?
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap  # the current node is now located here, for continuity
            childOneIdx = currentIdx * 2 + 1
        else:
            return


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


""" Question 7: Radix sort 
     Method :  0(d * (n+b)) time | 0(n + b) space - where n is the length of the input array,
        d is the max number of digits, and b is the base of the numbering system used
    - Radix sort behaves differently when array contains negative numbers (disadvantage) 
    because it considers the digits (tenth, hundreth, thousandth of numbers )
    - It requires that we know the maximum number length
    Example: [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
    - Initialize a count array that contains default zeros of length base. Since we're dealing with base10,
                    0,1,2,3,4,5,6,7,8,9
        count = [0,0,0,0,0,0,0,0,0,0]
    - Initialize a sorted array that contains default zeros of length of input array. e.g 9 elements.
        sorted = [0,0, 0,0,0,0,0,0,0]
    - In the count array, increment the counts index by the digit frequency. 
                    0,1,2,3,4,5,6,7,8,9
        count = [0,0,3,0,2,2,0,1,1,0]
        Now, starting at idx 1, sum adjacent numbers until the end
                    0,1,2,3,4,5,6,7,8,9
        count = [0,0,3,3,5,7,7,8,9,9]
        Now, loop through the input array, going backwards ( inorder to main the previously sorted)
            In the initialized sorted array, the count array tells us where to place the current element, 
            by reducing the frequency in the count, the leftover frequency is the index we need to position the 
                current element in the sorted array.
        Now, update the original array
"""


def radixSort(array):
    if not array:
        return array

    maxNumber = max(array)

    digit = 0
    while maxNumber:
        countingSort(array, digit)
        digit += 1
        maxNumber = maxNumber // 10
    return array


def countingSort(array, digit):
    countArray = [0] * 10
    sortedArray = [0] * len(array)

    # count the digit frequencies
    digitColumn = 10 ** digit
    for num in array:
        # Extract the number at index
        countIndex = (num // digitColumn) % 10
        countArray[countIndex] += 1

    # sum adjacent frequencies
    for idx in range(1, len(countArray)):
        countArray[idx] += countArray[idx-1]

    # fill the sorted array with reverse from the last known array
    for idx in range(len(array)-1, -1, -1):
        countIndex = (array[idx] // digitColumn) % 10
        # substract the frequency
        countArray[countIndex] -= 1
        sortedIndex = countArray[countIndex]
        sortedArray[sortedIndex] = array[idx]

    # update the original input array
    for idx in range(len(array)):
        array[idx] = sortedArray[idx]


""" Question 8: Merge sort 
     Method : 0(nlogn) time | 0(n) space
     Create One sorted array from 2 sorted Array
     Recursively, 
            -. get middle,
            -. sort left, sort right - Recursive
            -. Merge left & right - Merge two sorted lists
"""


def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    mergeSort(left)
    mergeSort(right)

    merge_two_sorted(left, right, array)
    return array


def merge_two_sorted(a, b, arr):

    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1

        k += 1

    #   when one list has been exhuasted
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


""" Question 9: Count Inversion 
    Write a func that takes in an array, and returns the number of inversions in the array.
    An inversion occurs if for any valid indices i j => i < j and array[i] > array[j]
    Method 1: 0(n^2) time | 0(1) space
        Compare every element with its post-ceding values
    Method 2: 0(nlogn) time | 0(n) space
        Using Merge sort, when current value in the left hand array is larger than right, then every values
        after it plus it is inverted. count all as inverted ,
"""


def countInversions(array):
    # 0(n^2) time | 0(1) space
    countInversion = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                countInversion += 1
    return countInversion


def countInversions(array):
    #  0(nlogn) time | 0(n) space

    return
