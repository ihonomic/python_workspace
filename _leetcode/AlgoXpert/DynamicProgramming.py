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

    Method: 

"""
