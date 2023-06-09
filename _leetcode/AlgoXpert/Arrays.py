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
            output[i] = smallest**2
            l += 1
        else:
            output[i] = largest**2
            r -= 1

    return output


""" Question 4 - An algorithm challenge, Given an array of pairs team who competed, and array of the result in (0 & 1), If 1 = Home won, 0 = Away won. 
    Return the overall best team. The one with the most wins, asumming each win is 3 points
    Method 1 - Use hashmap to save the bestTeam, 
    e.g: competitions=[
        ['HTML', 'C#'], 
        ['C#', 'Python'], 
        ['Python', 'HTML']
    ] 
    results=[0, 0, 1]     --> "Python"

"""


def tournamentWinner(competitions, results):
    # 0(n) time, 0(k) space - where n is number of competitions, k is number of teams
    # hash the winners points

    bestTeam = ""
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


""" Question 5: Non-constructible chnage . 
    Given an array of positive integers representing a the coins in your possession, write a function that returns the minimum sum of change
    that you CANNOT create. The array is not unique
    
    e.g [] --> 1
         [1,2,5] --> 4
         [5, 7, 1, 1, 2, 3, 22] --> 20
    Method: 0(nlogn) time | 0(1) space
    - The minimum amount you cannot create is usually the next unavailable number after the sum of all least numbers before it 
    i.e if all numbers sums up, we're unable to derive that number
"""


def nonConstructibleChange(coins):

    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        # i.e all the previous sums  didnt create this number and now we're currently at a number greater than it
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin

    return currentChangeCreated + 1


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

    for i in range(len(array) - 1):
        left = i + 1
        right = len(array) - 1
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


""" Question 7 -  Smallest Difference
    Given 2 arrays, returns the two numbers from each array whose absolute difference is closest to 0
            NOTE: The absolute difference of 2 integers is the distance between them on a real number line
            Consider Line number scale, diff = -5 and 5 = 10. diff = -5 and -4 = -1
        arr1 = [-1,5,10,20,28,3]
        arr2 = [26,134,135,15,17] solution => [28,26]
    Method 1 - 0(n * m) time, 0(1)space - Quadratic looping through arr1 and arr2, if the difference is lower than the last recorded difference,
                overrite it. Also overrite with both pair
    Method 2 - 0(nlongn + mlogm) time, 0(1) space - Sort the array. Two pointers. Until the left and right are within bounds. Continue to find the 
        difference between both sides nums, if 0, return pair, otherwise record it if is lower than the previous.
        
        we're shifting pointers because we are trying to obtain the closest difference to 0 
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
    smallest = float("inf")
    smallestPair = []

    while left < len(arrayOne) and right < len(arrayTwo):
        firstNum = arrayOne[left]
        secondNum = arrayTwo[right]

        if firstNum < secondNum:
            current = secondNum - firstNum
            left += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            right += 1
        else:
            return [firstNum, secondNum]  # if diff is 0.

        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair


""" Question 8 - Move element to end 
    Given an array, Move all occurrences of a target element to the end. The order of the elements doesn't matter.
    [2,1,3,2,4,2,1,2], toMove = 2. Solution => [1,3,4,1,2,2,2,2]
    Method 1 - Two pointers, On the left side keep looping until the target is found, on the right side keep looping until a non-target is
        found, swap them. 
"""


def moveElementToEnd(array, toMove):
    # This maintains the order
    elementIdx = 0
    for idx in range(len(array)):
        if array[idx] != toMove:
            swap(idx, elementIdx, array)
            elementIdx += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def moveElementToEnd(array, toMove):
    # 0(n) time, 0(1) space
    left, right = 0, len(array) - 1
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


""" Question 9 - Monotonic Array
    Given an array, Determine if it is Monotonic. 
    A monotomic array is that which continuously increasing or contineously decreasing. 
    Although similar adjacents elements is still regarded as being monotomic
    Method 1 - 0(n) time, 0(1) space.
        First Determine if the array is increasing or decreasing by the first 2 different elements. Use a flag
"""


def isMonotonic(array):
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

    for i in range(len(array) - 1):
        if is_increase and array[i] > array[i + 1]:
            return False

    return True


""" Question 9 - Spiral Matrix Traverse
    Given a 2D array, Collect all numbers into an array. 
    
    Method 1 - 0(n) time, 0(n) space.
        
"""


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
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # top
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # right
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # bottom
        for col in reversed(range(startCol, endCol)):
            # Make sure bottom != top -- CHECK ROW CONSTRAINT, IF YOU"RE COLLECTING COLUMN,
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # left
        for row in reversed(range(startRow + 1, endRow)):
            # Make sure left != right
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result


""" Question 9 - Longest Peak
    Write a function that takes in an array of integers and return the length of the longest peak in the array
    
    A peak is where the adjacents element is strictly increasing
    until they reach a tip(usually highest value in the peak), at which point they become strictly decreasing
    
    [1,4,10,2] is a peak
    [4,0,10] not a peak
    [1,2,2,0] not a peak
    [1,2,3] not a peak because there is any strictly decreasing after 3
    
    e.g : array=[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3] --> 6 // 0, 10, 6, 5, -1, -3
    The tip of a peak, is at the point where it was increasing and then decreases.
            l     p          r
    [1,2,3,3,4,0, 10, 6,5,-1,-3,2,3] -> 0,10,6,5,-1,-3, maxPeak= 6,
    there is a peak happening at 10
    Method 1 - 0(n) time, 0(1) space.
        - start from the second element
"""


def longestPeak(array):
    maxPeak = 0
    i = 1
    end = len(array) - 1  # we need i to stop before the last

    while i < end:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        # previous & current is not a start of a peak. Go FORWARD
        if not isPeak:
            i += 1
            continue

        # if previous and current is a peak, start expanding until the peak condition is broken or outofbounds
        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        peakLength = right - left - 1  # -1 because left expanded beyond what we want

        maxPeak = max(maxPeak, peakLength)

        # continue from where right stopped
        i = right
    return maxPeak


"""Question 12- Array of products 
    A function that returns an array of the same length, where each element in the output array
    is equal to the product of every other number in the input array
    [5,1,4,2] => [8, 40, 10, 20]
"""


def arrayOfProducts(array):
    output = []
    for i in range(len(array)):
        output.append(math.prod(array[0:i] + array[i + 1 :]))
    return output


"""Question 13 - First duplicate value 
    Given an array of integers between 1 and n, where n is the length of the array, return the number
    that is duplicated first.
    [2,1,5,2,3,3,4], 2 appeared first
    Method 1 - 0(n^2) time 0(1) space
    Method 2 - 0(n) time 0(n) space, Using hashSet or hashMap
    Method 3 - 0(n) time, 0(1) space 
        - By substracting each number from 1, it represent an index in the array,
        - Whatever number you find in the index, flag it as negative 
        - The next time you encounter a number at an index that's already negative, you know you've already seen the number that produces that index
"""


def firstDuplicateValue(array):
    # we're substracting 1 because we're dealing with' index and the questions says from 1-n
    for n in array:
        # get index
        absN = abs(n)
        if array[absN - 1] < 0:
            return absN
        array[absN - 1] *= -1

    return -1


""" Question 14 - Merge-overlapping intervals 

    e.g: [[1,2], [3,5], [4,7], [6,8], [9,10]] -> [[1,2], [3,8], [9,10]] 
    [[1,4], [6,9], [5, 10]] --> [1,10]
    Method : 0(nlogn) time and 0(n) space
        - Compare the incoming interval to the last saved interval. 
        - If the start of the incoming is less than/equal to the end of the last saved, overrite the last saved with the maximum ends of incoming and last saved. 
"""


def mergeOverlappingIntervals(intervals):

    intervals.sort(key=lambda x: x[0])
    output = []
    idx = 0

    while idx < len(intervals):
        if not output:
            output.append(intervals[idx])
        else:
            # if the start of the current interval is less than or equal to the end of the last saved
            if intervals[idx][0] <= output[-1][1]:
                output[-1][1] = max(intervals[idx][1], output[-1][1])
            else:
                output.append(intervals[idx])

        idx += 1

    return output


""" Question 15 -  Zero sum subarray
    Given an array of intergers, write a func that returns a boolean if there is a subarray whos 
    sum is equal to zero (0)

    e.g: [-5,-5, 2, 3, -2] --> True // [-5, 2, 3]
    
    Method 1 - 0(n^2) time | 0(n^2) space

    Method 2 - 0(n) time | 0(n) space 
        sums = set([0, -5, -10, -8, -5, ....])
                    [-5,-5, 2, 3, -2] 
        currentSum = [-5,-10, -8, -5, ...] 
        We found -5 again, which is already in the set. This means there must be a subarray which sums up to zero
        An index after our first -5 and the current -5 index is the subarray 
"""


def zeroSumSubarray(nums):
    if 0 in nums:
        return True

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            subArray = nums[i : j + 1]
            if sum(subArray) == 0:
                return True

    return False


def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False


""" Question : 3 Sum
    Return all combination of numbers from the array that equals to targetSum

    Method : 0(n^2)time, 0(n)space 
    
"""


def threeNumberSum(array, targetSum):
    result = []

    array.sort()

    for i in range(len(array) - 1):
        left = i + 1
        right = len(array) - 1
        while left < right:
            calcd = array[i] + array[left] + array[right]
            if calcd == targetSum:
                result.append([array[i], array[left], array[right]])

                left += 1
                right -= 1

            if calcd > targetSum:
                right -= 1
            if calcd < targetSum:
                left += 1

    return result


""" Question 15 - 4sum

    Method : 0(n^3) time, 0(n^2) space
    - Like 3 sum, a double for-loop before searching with pointers.
"""


def fourNumberSum(array, targetSum):

    output = []
    array.sort()

    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):

            l, r = j + 1, len(array) - 1

            while l < r:
                curr = [array[i], array[j], array[l], array[r]]
                currSum = sum(curr)
                if currSum == targetSum:
                    if curr not in output:
                        output.append(curr)
                    l += 1
                    r -= 1
                elif currSum > targetSum:
                    r -= 1
                elif currSum < targetSum:
                    l += 1
    return output


""" Question 16 - Subarray sort
    Given an array, return the start and end indexes of the smallest subarray from the input that need to be sorted to
    make the entire array sorted. If the entire is already sorted, return [-1, -1]
    e.g : [0,1,2,5,4,7,3,6,8,9],--> [3, 7]
    The subarray =[5,4,7,3,6] need to be sorted to make the entire array sorted
    
    Method 1: 0(n) time | 0(1) space
        Note: if one number is found unsorted, that means two is unsorted, 
        The subarray is dependent on the values that are out of order.
            (where the min and max values are suppose to be)
    - The idea is to find the minimum and maximum value that are out of order.
    - Find the position index of where both the minimum value and maximum value are
        suppose to be
"""


def subarraySort(array):

    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        # A number is out of order if the prev is greater than it or it is greater than the previous
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    # check if any outofOrder was found
    if minOutOfOrder == float("inf"):
        return [-1, -1]

    # Now, find the position index
    # where the minumum and maximum out of order is suppose to be
    subarrayMinIdx = 0
    while minOutOfOrder >= array[subarrayMinIdx]:
        subarrayMinIdx += 1

    subarrayMaxIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayMaxIdx]:
        subarrayMaxIdx -= 1

    return [subarrayMinIdx, subarrayMaxIdx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return array[i - 1] > num or num > array[i + 1]

""" Question 17 - Transpose Matrix
    Given a 2D array of intergers matrix. Write a func that returns the transpose of the matrix. 
    NOTE: Transpose of a matrix, the rows becoming columns and vice versa. 

    e.g : [
    [1, 2],
    [3, 4],
    [5, 6],]
    -->
      [
    [1, 3, 5],
    [2, 4, 6],
    ]
    
    Method : 0(n * h) time | 0(n * h) space
        We need to go inside the column for every row and 
        add to a new array which will later be added to our result
"""

def transposeMatrix(matrix):

    result = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])

        result.append(newRow)
    return result 
