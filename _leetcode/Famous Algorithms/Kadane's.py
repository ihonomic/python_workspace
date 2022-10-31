""" 
- This algorithm is used to find the maximum subarray in a given array. 
- Assuming there are no negative values, the maximum is sum of the given array. 
- But in this case there there are negative numbers in the array, using dynamic programming. 
    Find the sum so far, compare with the current. Keep track of the all-time largest sum 
"""


def kadanesAlgorithm(array):
    maximumSumHere = array[0]
    maximumSoFar = array[0]

    for i in range(1, len(array)):
        curr = array[i]
        maximumSumHere = max(maximumSumHere + curr, curr)
        maximumSoFar = max(maximumSoFar, maximumSumHere)

    return maximumSoFar


print(kadanesAlgorithm(
    [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))  # 19
