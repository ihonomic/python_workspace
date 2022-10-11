#   Copyright ©2022 - Ihon Oseghale

""" Question 1 - TARGET SUM:  Given an array and target sum, return array of the 2 intergers that sums up to target
    array = [1,3,5,-4], t = 8. Solution => [3,5]
        Method 1 - 0(n^2) time, 0(1) space - Two loops
        Method 2 - 0(n) time, 0(n) space - Using hashmap 
        Method 3 - 0(nlogn) time, 0(1) space - Like 3sum problem, Sort the array, Two pointers. while first < last 
                    if first+last > target, reduce right or otherwise.
"""

""" Question 2 - isValidSubsequence: Given an array & another array of potential subsequence, check if the potential subsequence is a valid
    subseqeuence of the main array. 
    array = [5,6,8,2,0,5,7], subsequence = [5,8,7]. Solution => Returns True, because the subsequence 5,8,7 are exactly in the order of the main array
        Method 1 - 0(n) time, 0(1) space - Two pointers, while the 'subsequence index' is still within bounds, increment both pointers, if equal, 
                    otherwise increment only 'array index'
"""




import math
def isValidSubsequence(array, sequence):
    # 0(n) time, 0(1) space, where n is length of array
    # Two pointers, let l = sequence, r = array
    l = r = 0

    while l < len(sequence) and r < len(array):
        if sequence[l] == array[r]:
            l += 1
            r += 1
            continue
        r += 1

    return l == len(sequence)


""" Question 3 - sortedSquaredArray: Given an array that is sorted, square each nums and return it sorted. Note there might be negative numbers
    array = [-6,2,3,4,5] => [4,9,16,25,36]
    Method 1 - 0(nlogn) time, 0(1) space - Loop & sqaure the numbers, replace it by array[i] = n **2, sort resulting array
    Method 2 - 0(n) time, 0(n) space - Two pointers, Initialize the array with 0s,  - Loop from end index
        if the absolute num at left-most index is greater than rightmost num, square the leftmost are insert, 
"""


def sortedSquaredArray(array):
    # 0(n) time, 0(n) space
    output = [0 for _ in range(len(array))]

    l, r = 0, len(array) - 1

    for i in reversed(range(len(array))):
        smallest = array[l]
        largest = array[r]

        if abs(smallest) > abs(largest):
            output[i] = smallest ** 2
            l += 1
        else:
            output[i] = largest ** 2
            r -= 1

    return output


""" Question 4 - An algorithm challenge, Given an array of pairs team who competed, and array of the result in (0 & 1), If 1 = Home won, 0 = Away won. 
    Return the overall best team. The one with the most wins, asumming each win is 3 points
    Method 1 - Use hashmap to save the bestTeam, 

"""


def tournamentWinner(competitions, results):
    # 0(n) time, 0(k) space - where n is number of competitions, k is number of teams
    # hash the winners points

    bestTeam = ''
    hashMap = {bestTeam: 0}

    for match, result in zip(competitions, results):

        result = 0 if result == 1 else 1  # swap the result index

        team = match[result]

        if team in hashMap:
            hashMap[team] += 3
        else:
            hashMap[team] = 3

        if hashMap[team] > hashMap[bestTeam]:
            bestTeam = team

    return bestTeam


""" Question 5

"""


def nonConstructibleChange(coins):
    # Write your code here.
    array = []

    for i in range(len(coins)-1):
        for j in range(i+1, len(coins)):
            array.append(coins[i] + coins[j])

    s = set(array + coins)

    print(s)
    max_ = max(s)
    for i in range(1, max_+1):
        if i not in s:
            return i
    return i + 1


print(nonConstructibleChange([1, 2, 4, 7]))

""" Question 6 - 3sums. Given an unsorted array and a target, return all the triplets nums that sums upto target in a sorted order
    [12,3,1,2,-6,5,-8,6], target = 0 => Solution=> [[-8,2,6], [-8,3,5], [-6, 1,5]]  
    Method 1: Like 2sums, you can use hashMap or cubic time 0(n^3), 3 loops. 
    Method 2: Loop through, for every index, while loop two pointers at the next index from current index, (sum current index, and left and end pointer)
            Keep moving the pointers until target sum is found, else break out from the loop and move over to the next index
            0(n^2)time, 0(n)space 
    Method 3: Use the combinations method from itertools
"""


def threeNumberSum(array, targetSum):
    # 0(n^2)time, 0(n)space
    result = []

    array.sort()

    for i in range(len(array)-1):
        left = i+1
        right = len(array)-1
        while left < right:
            calcd = array[i] + array[left] + array[right]  # <== FORMULAR POINT
            if calcd == targetSum:
                result.append([array[i], array[left], array[right]])

                left += 1
                right -= 1

            if calcd > targetSum:
                right -= 1
            if calcd < targetSum:
                left += 1

    return result


""" Question 7 - Given 2 arrays, returns the two numbers from each array that resulted to the least difference.
            NOTE: Consider Line number scale, diff = -5 and 5 = 10. diff = -5 and -4 = -1
        arr1 = [-1,5,10,20,28,3]
        arr2 = [26,134,135,15,17] solution => [28,26]
    Method 1 - 0(n * m) time, 0(1)space - Quadratic looping through arr1 and arr2, if the difference is lower than the last recorded difference,
                overrite it. Also overrite with both pair
    Method 2 - 0(nlongn + mlogm) time, 0(1) space - Sort the array. Two pointers. Until the left and right are within bounds. Continue to find the 
        difference between both sides nums, if 0, return pair, otherwise record it if is lower than the previous.
"""


def smallestDifference(arrayOne, arrayTwo):
    #   Method 1
    # 0(n * m) time, 0(1) space

    value = float("inf")
    result = []

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            substract = (arrayOne[i]) - (arrayTwo[j])
            abst = abs(substract)

            if abst < value:
                value = abst
                result = [arrayOne[i], arrayTwo[j]]

    return result

    #   Method 2.
    # 0(nlongn + mlogm) time, 0(1) space

    arrayOne.sort()
    arrayTwo.sort()

    left = right = 0
    smallest = float('inf')
    smallestPair = []

    while left < len(arrayOne) and right < len(arrayTwo):
        firstNum = arrayOne[left]
        secondNum = arrayTwo[right]

        if firstNum < secondNum:
            current = (secondNum) - (firstNum)
            left += 1
        elif secondNum < firstNum:
            current = (firstNum) - (secondNum)
            right += 1
        else:
            return [firstNum, secondNum]   # if diff is 0.

        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair


""" Question 8 - Given an array, Move all occurrences of a target element to the end. The order of the elements doesn't matter.
    [2,1,3,2,4,2,1,2], toMove = 2. Solution => [1,3,4,1,2,2,2,2]
    Method 1 - Two pointers, On the left side keep looping until the target is found, on the right side keep looping until a non-target is
        found, swap them. 
"""


def moveElementToEnd(array, toMove):
    # 0(n) time, 0(1) space
    left, right = 0, len(array)-1
    while left <= right:
        #   if not target, please move to next, same idea to skip duplicated number in a rotated array with duplicates.
        while left < right and array[left] != toMove:
            left += 1
        while left < right and array[right] == toMove:
            right -= 1

        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    return array


""" Question 9 - Given an array, Determine if it is Monotonic. 
    A monotomic array is that that is continuously increasing or contineously decreasing. 
    Although similar adjacents elements is still regarded as being monotomic
    Method 1 - Determine if the array is increasing or decreasing by the first 2 different elements. Use a flag
"""


def isMonotonic(array):
    # 0(n) time, 0(1) space.
    # - take care of empty or single element array, they're monotonic
    # - Determine if elements are increasing or non-decreasing with a flag
    # - if increasing, the next element is lower than the current element return false

    if len(array) <= 2:
        return True

    is_increase = False

    l, r = 0, 1
    while r < len(array):
        if array[l] < array[r]:
            is_increase = True
            break
        l += 1
        r += 1

    for i in range(len(array)-1):
        if is_increase and array[i] > array[i+1]:
            return False

    return True


def spiralTraverse(array):
    """
    [
            sC       eC
        sR [1, 2, 3, 4]
           [12,13,14,5]
           [11,16,15,6]
        eR [10, 9, 8,7]
    ]

    result => [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    """
    result = []
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # top
        for col in range(startCol, endCol+1):
            result.append(array[startRow][col])

        # right
        for row in range(startRow+1, endRow+1):
            result.append(array[row][endCol])

        # bottom
        for col in reversed(range(startCol, endCol)):
            # Make sure bottom != top
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # left
        for row in reversed(range(startRow+1, endRow)):
            # Make sure left != right
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result


def longestPeak(array):
    ''' Find the longest peak in an array. A peak is where the adjacents element is strictly increasing
    until they reach a tip(highest value in the peak), at which point they become strictly decreasing.

    The tip of a peak, is at the point where 
    it was increasing and then decreases.  
             l     p          r
    [1,2,3,3,4,0, 10, 6,5,-1,-3,2,3] -> 0,10,6,5,-1,-3, maxPeak= 6, 
    there is a peak happening at 10
    '''
    maxPeak = 0
    i, end = 1, len(array)-1

    while i < end:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue
        # left
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        # right
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeak = rightIdx - leftIdx - 1
        maxPeak = max(maxPeak, currentPeak)

        i = rightIdx
    return maxPeak


"""Question 12- A function that returns an array of the same length, where each element in the output array
is equal to the product of every other number in the input array
[5,1,4,2] => [8, 40, 10, 20]
"""


def arrayOfProducts(array):
    output = []
    for i in range(len(array)):
        output.append(math.prod(array[0:i] + array[i+1:]))
    return output


"""Question 13 - First duplicate value - Given an array of integers between 1 and n, where n is the length of the array, return the number
that is duplicated first.
[2,1,5,2,3,3,4], 2 appeared first
Method 1 - 0(n^2) time 0(1) space
Method 2 - 0(n) time 0(n) space, Using hashSet or hashMap
Method 3 - 0(n) time, 0(1) space - Mark each element to negative by their index, the next time you encounter a negative value at the index that
the integer maps to you know that you've already seen that interger
"""


def firstDuplicateValue(array):
    for n in array:
        # get index
        absN = abs(n)
        if array[absN - 1] < 0:
            return absN
        array[absN-1] *= -1

    return -1
