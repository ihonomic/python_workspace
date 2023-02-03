""""
 Dynamic Programming is solving smaller problems and using the solution to solve larger problems
 - STEPS:
 - Build an array similar to the input array
"""
from math import factorial

""" Question 1: Max Subset sum no adjacent
    Write a func that takes an array of positive intergers and return the maximum sum of non-adjacents elements
    in the array. Return 0 if input array is empty. 
    
     COMPUTE THE MAXIMUM SUM OF ELEMENTS THAT ARE NOT ADJACENT TO EACH OTHER 
    
    e.g: [75, 105, 120, 75, 90, 135] --> 75 + 120 + 135 = 330
    Method: 0(n) time | 0(n) space
    - Keep deriving the maximum sum at each index
    - NOTE: for the first index, the maximum sum is itself.
    - But for the second index, the maximum sum is the largest btw previous or current.
    - Then for subsequents indexes, the maximum sum is the largest btw previous or the element before previous plus current
    
    Method 2: 0(n) | 0(1) space 
"""


def maxSubsetSumNoAdjacent(array):
    # formular - fibonacci sequence
    # maxSum(i) = max(maxSums[i-1], maxSums[i-2] + array[i])

    if not array:
        return 0

    if len(array) == 1:
        return array[0]

    maxSums = [0 for _ in array]
    maxSums[0] = array[0]
    maxSums[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])

    return maxSums[-1]


def maxSubsetSumNoAdjacent(array):
    prev, curr = 0, 0

    for num in array:
        prev, curr = curr, max(curr, prev + num)
    return curr


""" Question 2: Number of ways to make a chnage 
    Given an array of distinct positive integers, representing coin denominations and a single positive integer n,
    representing target amount of money, 
    Write a func that return the number of ways to make change for that target amount using the given coin denominations
    
    NOTE: An unlimited amount of coins is at ur disposal. 
    
    e.g:   n = 6 
            denoms = [1,5] --> 2 // 
                (coin x number of times)
                1x1 + 1x5 
                6x1
            
            n = 10 
            denoms = [1,5,10,25] --> 4 // 
                1x10
                5x2
                1x5 + 5x1
                10x1
            
    Method: 0(nd) time | 0(n) space
        
        # n=10 denoms=[1, 5, 10, 25]
    
        # Define skeleton 
        ways = [0 for _ in range(n + 1)]
        ways[0] = 1
        
        # ways = [1,0,0,0,0,0,0,0,0,0,0]
        # coin  = 0,1,2,3,4,5,6,7,8,9,10
        # from the above, you'll see that there is only 1way to make 0 coin change, 
        # We go through each demon, if the denom is less than or equal to the current change, that means that denom
        # can form the given chnage, update the ways (ways[change] += ways[change - denom])
    
        # When denom = 1, it can generate all amounts to 10
        # waysToMakeChange = [1,1,1,1,1,1,1,1,1,1,1]
    
        # When denom = 5, it can generate from 5 to 10 change
        # waysToMakeChange = [1,1,1,1,1,2,2,2,2,2,3]
    
        # When denom = 10, it can generate only 10 chnage
        # waysToMakeChange = [1,1,1,1,1,2,2,2,2,2,4]
    
        # When denom = 25, it will NEVER generate any change
        # waysToMakeChange = [1,1,1,1,1,2,2,2,2,2,4]
"""


def numberOfWaysToMakeChange(n, denoms):
    # ways[change] += ways[change - denom]

    # skeleton
    waysToMakeChange = [0 for _ in range(n + 1)]
    waysToMakeChange[0] = 1  # Number of ways to make 0 is 1

    for denom in denoms:
        for change in range(1, n + 1):
            # can we use denom to make this change?
            if denom <= change:
                waysToMakeChange[change] += waysToMakeChange[change - denom]

    # print(waysToMakeChnage)
    return waysToMakeChange[n]


""" Question 3: Minimum number of coins for change
    Given an array of distinct positive integers, representing coin denominations and a single positive integer n,
    representing target amount of money, 
    Write a func that return the minimum counts of coins to make change for that target amount using the given coin 
    denominations
    
    e.g: n = 7 
         denoms = [1,5,10]  --> // 3
                            3 coins can form 7 (1x2, 5x1 ==> 1,1,5)
                            
    Method: 0(nd) time | 0(n) space 
        If we see that a particular denom can make the current change/amount,
         we update the coins count for that change/amount
"""


def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for _ in range(n + 1)]
    numOfCoins[0] = 0  # To make 0 change, we need 0 coins

    for denom in denoms:
        for change in range(1, n + 1):
            # can we use denom to make this change?
            if denom <= change:
                numOfCoins[change] = min(
                    numOfCoins[change], 1 + numOfCoins[change - denom]
                )

    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


""" Question 4 -Number of ways to traverse a Graph
    You're given 2 positive integers representing the width & height of a grid-shaped, rectangular graph.
    Write a func that returns the number of ways of reach the bottom right corner if movement starts from 
    the top-left corner. 
    
    NOTE: Each movement you take must either go down or right. (You CANNOT move up or left). 
    GRAPH WILL NEVER BE 1x1 grid
    e.g width = 2, height= 3
                    _  _
                   |_|_|
                   |_|_|
                   |_|_|
        --> 3 ways
        - down, down, right
        - right, down, down
        - down, right, down
    Method: Recursion. 0(2^(n+m)) time | 0(n + m) space 
        Number of ways to get to the far bottom-right corner will be sum of the ways to get to both 
        left and top before the bottom-right corner (. :) and this also applies to every other box 
    Method: Dynamic Programming. 0(n*m) time | 0(n*m) space 
        Same way. Figure out the way to get to the neighbors. Save the intermediate results.
        Remember at the borders, there is always one way to get to them. 
    Method: Permutations 0(n+m) time | 0(1) space 
         We can calculate the number of ways to get to the bottom-right corner by determining the number of right  and 
         down movements. 
         From the grid above, number of RIGHT = width - 1, number of DOWN = height - 1
         {R, D, D} and the count of the possible permutations of it becomes;
                 {R, D, D}
                 {D, R, D}
                 {D, D, R} --> 3 ways 
        Forumular for Permutations of two cases :
            (R + D)! / R! * D!                               
"""


def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1

    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(
        width, height - 1
    )


def numberOfWaysToTraverseGraph(width, height):
    # Assuming width =4 height = 3
    # There is only one way to get to boxes at the borders
    numberOfWays = [[1 for _ in range(width)] for _ in range(height)]
    # [
    #     [1, 1, 1, 1],
    #     [1, 2, 3, 4],
    #     [1, 3, 6, 10]
    # ]

    for heightIdx in range(1, height):
        for widthIdx in range(1, width):
            # add the left and top
            waysLeft = numberOfWays[heightIdx][widthIdx - 1]
            waysUp = numberOfWays[heightIdx - 1][widthIdx]

            numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

    return numberOfWays[-1][-1]


def numberOfWaysToTraverseGraph(width, height):
    #    (R + D)! / R! * D!
    right = width - 1
    down = height - 1

    numerator = factorial(right + down)
    denominator = factorial(right) * factorial(down)

    return numerator / denominator


""" Question 5 - Levenshtein distance
    You are given two strings s1 and s2. Write a function that returns the minimum number of edit operations to be performed
    on the first string s1, to obtain s2. 

    NOTE: There are three operations. Insertion, deletion and substitution of a character for another. 
    e.g: str1 = "abc" 
          str2 = "yabd"
    --> 2 // insert "y" ; substitute "c" for "d"

    Method:  0(nm) time | 0(nm) space
        editTable - 2D number of operations to perfom to turn s1 into s2 
         s1 = abc s2 = yabd
            "" y a b d 
        ""  0  1 2 3 4
        a   1  1 1 2 3
        b   2  2 2 1 2
        c   3  3 3 2 2

        - Consider empty strings
        - if horizontal char is equal to vertical char, choose the diagonal value
        - BUT whenever a horizontal char is being compared with the vertical char, 
        just consider 3 neigbors value, pick the minimum & add 1

        if str1[row-1] == str2[col-1]:
            editTable[row][col] = editTable[row-1][col-1]
        else:
            editTable[row][col] = 1 + min(
                                        editTable[row][col-1], 
                                        editTable[row-1][col], 
                                        editTable[row-1][col-1], 
                                        )
"""


def levenshteinDistance(str1, str2):
    # Assuming str1="abc", str2="yabd"
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    # [
    #     [0, 1, 2, 3],
    #     [0, 1, 2, 3],
    #     [0, 1, 2, 3],
    #     [0, 1, 2, 3],
    #     [0, 1, 2, 3]
    # ]
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    # [
    #     [0, 1, 2, 3],
    #     [1, 1, 2, 3],
    #     [2, 1, 2, 3],
    #     [3, 1, 2, 3],
    #     [4, 1, 2, 3]
    # ]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(
                    edits[i][j - 1], edits[i - 1][j], edits[i - 1][j - 1]
                )
    # [
    #     [0, 1, 2, 3],
    #     [1, 1, 2, 3],
    #     [2, 1, 2, 3],
    #     [3, 2, 1, 2],
    #     [4, 3, 2, 2]
    # ]

    return edits[-1][-1]


""" Question 6 - Max Sum Increasing Subsequence
Write a func that takes an array of integers and returns the greatest sum that can be generated from a STRICTLY
INCREASING SUBSEQUENCE in the array. (Unlike kadane, there can be negative values and not strictly increasing)

NOTE: Each element is a subsequence of its array, so also its a set of numbers that aint necessary adjacent but maintain the 
    order. [1,3,4] is a subsequence of [1,2,3,4,5]

e.g:  array=[10, 70, 20 ,30, 50, 11, 30] --> 110, [10, 20, 30, 50 ]
Method: 0(n^2) time | 0(n) space
    The idea: For every index, determine the maximum sum including itself at that point
    i.e compare current number with numbers starting from the beginning to current

"""


def maxSumIncreasingSubsequence(array):

    # Build 1
    # stores the indexes
    sequences = [None for _ in array]

    # Build 2
    # stores the greatest sum subsequence at each index
    sums = array[:]

    maxSumIdx = 0

    for i in range(len(array)):
        currentNum = array[i]
        # check previous numbers before it
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j

        # Is the current idx the greatest sum? Record it
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    return [max(sums), buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):

    result = []
    # end when currentIdx becomes None
    while currentIdx is not None:
        result.append(array[currentIdx])
        currentIdx = sequences[currentIdx]

    return result[::-1]  # reverse it because it values were appended from the last


""" Question 7 - Longest common subsequence
Write a func that takes two strings and returns their common subsequences


e.g:  str1='ZXVVYZW' str2='XKYKZPW' --> ["X", "Y", "Z", "W"]
Method: 0(nm) time | 0(nm) space

"""


def longestCommonSubsequence(str1, str2):
    # Assume str1='ZXVVYZW' str2='XKYKZPW'
    commonStrs = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    # [
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '']
    # ]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # if both strings character are same, take the diagonal and append with current
            if str1[i - 1] == str2[j - 1]:
                commonStrs[i][j] = commonStrs[i - 1][j - 1] + str1[i - 1]
            else:
                top = commonStrs[i - 1][j]
                left = commonStrs[i][j - 1]
                # choose the longest string from the left & top neighbor
                commonStrs[i][j] = max(top, left, key=len)

    # [
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', 'Z', 'Z', 'Z'],
    #     ['', 'X', 'X', 'X', 'X', 'Z', 'Z', 'Z'],
    #     ['', 'X', 'X', 'X', 'X', 'Z', 'Z', 'Z'],
    #     ['', 'X', 'X', 'X', 'X', 'Z', 'Z', 'Z'],
    #     ['', 'X', 'X', 'XY', 'XY', 'XY', 'XY', 'XY'],
    #     ['', 'X', 'X', 'XY', 'XY', 'XYZ', 'XYZ', 'XYZ'],
    #     ['', 'X', 'X', 'XY', 'XY', 'XYZ', 'XYZ', 'XYZW']
    # ]

    return list(commonStrs[-1][-1])


""" Question 8 - Minimum Number of Jumps
Given an array of positive integers where each interger represents the maximum number of steps forward in the 
array. For example if the element at index 1 is 3, you can go from index 1 to index 2, 3, or 4.

Write a func that returns the minimum number of jumps needed to reach the final index. 

NOTE; Jumping from index i to index i + x always constituents one jump, no matter how large x is.
e.g:  array =[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3] --> 4 // 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
Method: 0(n^2) time | 0(n) space
     for every current index, check from the beginning if we can jump to the current
     
Method: 0(n) time | 0(1) space

"""


def minNumberOfJumps(array):
    # [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    # 3 -> 4 -> 3 -> 7

    jumps = [float("inf") for _ in array]

    # To jump to the first is 0 jumps
    jumps[0] = 0

    # for every current index,
    # check from the beginning if we can jump to the current
    for i in range(1, len(array)):
        for j in range(0, i):
            # can you reach i from j?
            if array[j] + j >= i:
                jumps[i] = min(jumps[j] + 1, jumps[i])

    return jumps[-1]


def minNumberOfJumps(array):
    if len(array) == 1:
        return 0

    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):  # we don't need to get to final index
        maxReach = max(maxReach, array[i] + i)
        steps -= 1

        # Are we out of steps?
        if steps == 0:
            jumps += 1
            steps = (
                maxReach - i
            )  # how many steps do we need to get to maxReach from current position?

    return jumps + 1


""" Question 9 - Knapsack problem
    An array of items(array). Each item array has two values, the first represent it's value
    and the second represent its weight. 
    You're also given a value which represent the maximum weight capacity

    Fit into the knapsack items of maximized values and make sure the sum of their weights doesn't 
    exceed maximum weight capacity 

    Consider their combined value as you pick, as well as each item indices of how you 
    intend to arrange them in the knapsack

    Write a function that returns the maximized combined value of the items and the chosen item indices
    e.g:  items=[[1,2], [4,3], [5,6], [6,7]] capacity=10
                       [value(v), weight(w)] 
                    -->  [
                            10, // total value 
                            [1, 2], // item indices
                        ]

    Method: 0(nc) time | 0(nc) space - c is the maximum capacity 

"""


def knapsackProblem(items, capacity):
    # items=[[1,2], [4,3], [5,6], [6,7]] capacity=10
    # [value(v), weight(w)]

    knapsackValues = [
        [0 for _ in range(0, capacity + 1)] for _ in range(len(items) + 1)
    ]

    #  (w)     0 1 2 3 4 5 6 7 8 9 10
    # [ ]       0 0 0 0 0 0 0 0 0 0 0
    # [1,2]   0 0 0 0 0 0 0 0 0 0 0
    # [4,3]   0 0 0 0 0 0 0 0 0 0 0
    # [5,6]   0 0 0 0 0 0 0 0 0 0 0
    # [6,7]   0 0 0 0 0 0 0 0 0 0 0

    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]  # i-1 because of the additonal row
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(
                    knapsackValues[i - 1][c],
                    knapsackValues[i - 1][c - currentWeight] + currentValue,
                )

    #  (w)    0 1 2 3 4 5 6 7 8 9 10
    # [ ]     0 0 0 0 0 0 0 0 0 0 0
    # [1,2]   0 0 1 1 1 1 1 1 1 1 1
    # [4,3]   0 0 1 4 4 5 5 5 5 5 5
    # [5,6]   0 0 1 4 4 5 5 5 6 9 9
    # [6,7]   0 0 1 4 4 5 5 6 6 9 10

    # EXPLANATION: if the current item's weight is less than the weight being considered (w).
    # That means it can fit into the bag, but we need to know if it can fit together
    # with the previous item. PRIORITY: choose the one with maximum value

    # Choose the maximum between the top and the current value(added to the top - weight)

    # if w <= j:
    # values[i][j] = max(
    #             values[i-1][j],
    #             values[i-1][j-w] + v,
    #         )
    # else:
    # values[i][j] = values[i-1][j]

    return [knapsackValues[-1][-1], getknapsackItems(knapsackValues, items)]


def getknapsackItems(knapsackValues, items):
    # TO GET THE ITEMS indices THAT WAS CHOOSEN
    # We need to backtrack, our item can only be considered in the bag if
    # the value isnt the same as that at the top

    # We keep moving top if current value is the same as the top, else, we add item because the item was
    # used, we move top but left-side of the top - weight. This continue until we jump to
    # the first row
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)  # because we've additonal row
            c -= items[i - 1][1]
            i -= 1
    # because, we built sequence using backtracking, so we reverse it
    sequence.reverse()

    return sequence


""" Ones and Zeros
    Given an array of binary strings strs and 2 intergers m & n . 
    Return the size of the largest subset of strs  such that there are at most m 0's & n 1's in the subset. 

    e.g:  strs = ["10","0001","111001","1","0"], m = 5, n = 3   --> 4 // {"10", "0001", "1", "0"}
            strs = ["10","0","1"], m = 1, n = 1  -->  2 // {"0", "1"}

    Method: 

"""


def findMaxForm(strs: list, M: int, N: int) -> int:
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    # [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0]
    # ]
    for char in strs:
        zeros = char.count("0")
        ones = char.count("1")
        for i in range(M, zeros - 1, -1):
            for j in range(N, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

    # [
    #     [0, 1, 1, 1],
    #     [1, 2, 2, 2],
    #     [1, 2, 3, 3],
    #     [1, 2, 3, 3],
    #     [1, 2, 3, 3],
    #     [1, 2, 3, 4]
    # ]

    return dp[-1][-1]


# Bounded 0/1 Knapsack problems
# LC 416. Partition Equal Subset Sum
# LC 494. Target Sum
# LC 474. Ones and Zeroes
# LC 343. Integer Break

# Unbounded 0/1 Knapsack problems
# LC 322. Coin Change
# LC 518. Coin Change 2
# LC 377. Combination Sum IV
# LC 983. Minimum Cost For Tickets


""" Question 10 - Disk Stacking
    Given an array of arrays where each subarrays hold 3 integers and represent a disk. The intergers are the weight, depth & height
    respectively. Your goal is to stack up the disks and maximize the total height of the stack. A disk must have a strictly 
    smaller width, depth & height than any other disk below it. 

    Write a func that returns an array of the disks in the final stack starting with the top disk and ending with the bottom disk.
    Note that you can't rotate disks. i.e the intergers in each subarray must represent [width, depth, height] at all times.
    e.g:  [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]] -->  [[2, 1, 2], [3, 2, 3], [4, 4, 5]]
        // 10 (2+3+5) is the tallest height we can get 
    NOTE: Each width, depth & height is ascending 
    Method: 0(n^2) time | 0(n) space

"""


def diskStacking(disks):
    # [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    # Sort the disks by their height
    disks.sort(key=lambda disk: disk[2])
    # [[1, 3, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]

    # store the heights in another array
    heights = [disk[2] for disk in disks]
    # [1, 2, 3, 4, 5, 8]

    # store the index of the previous disk that comes ontop of another one
    sequences = [None for disk in disks]
    # [None, None, None, None, None, None]

    # keep track of the maximum height
    maxHeightIdx = 0

    # compare previous disks with the current disk and ensure w, d & h are valid
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            sumOfHeights = currentDisk[2] + heights[j]
            isCurrentHeightLessOrEqualToBoth = heights[i] <= sumOfHeights
            if (
                areValidDimensions(otherDisk, currentDisk)
                and isCurrentHeightLessOrEqualToBoth
            ):
                # it's valid, update the height of current disk
                heights[i] = sumOfHeights
                # keep track of the otherDisk index that is valid but at the currentDisk location
                sequences[i] = j

        # update the maximum height found
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i

    # disks=[[1, 3, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]
    # heights=[1, 2, 5, 4, 10, 8]
    # sequences=[None, None, 1, None, 2, None]

    return buildSequence(disks, sequences, maxHeightIdx)


def areValidDimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def buildSequence(array, sequences, currentIdx):
    # sequences=[None, None, 1, None, 2, None]
    result = []
    while currentIdx is not None:
        result.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    # [bottomDisk, secondBottomDisk, thirdBottomDisk,... topDisk]
    return list(reversed(result))


""" Question 11 - Numbers in Pi 
    Given a string representations of the first n digits in pi and a list of positive intergers (all strings formats), write a func that returns 
    the smallest number of spaces that can be added to the n digits of pi such that all resulting numbers are found in the list of integers.

    NOTE: A single number can appear multiple times in the resulting numbers. For example, if pi is "3141" and the numbers are ["1", "3", "4"  ], 
    the number "1" is allowed to appear twice in the list of resulting numbers after 3 spaces are added:  " 3 | 1 | 4 | 1".
    If no number of spaces to be added exists such that all resulting numbers are found in the list of integers, the function should return -1 

    e.g pi='3141592653589793238462643383279' 
        numbers=['314159265358979323846', '26433', '8', '3279', '314159265', '35897932384626433832', '79']
    --> 2 // '314159265', '35897932384626433832' , '79'
"""
