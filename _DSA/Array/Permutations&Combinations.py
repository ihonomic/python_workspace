""" Question : Next Permutation
    Given an array of integers nums, find the next permutation of nums.
    Return in place.                 NOTE: itertools.permutation can do this

    Input: nums = [1,2,3]
    Output: [1,3,2]

    Input: nums = [3,2,1]
    Output: [1,2,3]

    Input: nums = [1,1,5]
    Output: [1,5,1]
    METHOD :
    Given: [0,1,2,10,9,4,3,0]
        - Beginning from the end, Find the turning point in the array, (i.e: where the current element
        is less than the previous]. The first ascending point, if it doesn't exist, sort the entire array and
        return it.   [0,1,2, /  10,9,4,3,0]  . 2 is the turning point
        - If a turning point is found, we need to find a number from the end of the right side and swap with
        it.   [0,1,3, /  10,9,4,2,0]
        - Lastly, SORT the right side by reversing. [0,1,3, /  0,2,4,9,10]
"""


def nextPermutation(nums) -> None:
    length = len(nums)
    # if length is less/equal to 2, the next permutation is the reverse
    if length <= 2:
        nums.reverse()
        return nums

    # Begin from the last but one element, check for ascending
    rightIdx = length - 2
    while rightIdx >= 0 and nums[rightIdx] >= nums[rightIdx + 1]:
        rightIdx -= 1

    # This means all numbers are decending, the next permutation is going to be a reset
    # [3,2,1] --> [1,2,3]
    if rightIdx == -1:
        nums.reverse()
        return nums

        # We've found a turning point, now we need to find a number from the right side to swap
    # with the turnning point number, i.e it's the first number that is greater than it
    # from right far right
    for endIdx in range(length - 1, rightIdx, -1):
        if nums[rightIdx] < nums[endIdx]:
            swap(rightIdx, endIdx, nums)
            break

    # reverse the right side/ sort it. i.e before we got to rightIdx - end
    reverseRange(rightIdx + 1, length - 1, nums)

    return nums


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def reverseRange(startIdx, endIdx, array):
    while startIdx <= endIdx:
        swap(startIdx, endIdx, array)
        startIdx += 1
        endIdx -= 1


""" Question: Permutations
    Question: Permutations Unique
    Given an array nums of distinct integers, return all the possible permutations. 
    You can return the answer in any order.
    
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Method:
    BACKTRACKING 
        We keep on removing the first element for the next recursive element to form without it, 
        Until we encounter the base case. 
        Then we start appending the removed element to the various forms of returns
                        [1,2,3]
                        /     |     \
                    [2,3]   [1,3]  [1,2]
                    /    \       /  \      \  \
                [3]      [2]   [3] [1]   [2] [1]           --> 6 different cases
"""


def permuteUnique(nums) :
    result = []

    if len(nums) == 1:
        return [nums.copy()]  # form a new array and don't modify the main array

    for _ in range(len(nums)):
        # remove one element, recursively
        n = nums.pop(0)
        perms = permuteUnique(nums)

        # add the removed element to each permutations
        for perm in perms:
            perm.append(n)
            result.append(perm)  # TAKE NOTE: if the question demands it to be unique, check if a similar perm is not
            # already in result before add it

        # add the removed element to the end, for the next permutations
        nums.append(n)
    return result

