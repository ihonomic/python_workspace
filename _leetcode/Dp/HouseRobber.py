""" Question: House Robber 1
    You're a robber and wants to rob houses but you can't rob adjacent houses, what it is the maximum you can rob
    from that night?
    Input: nums = [1,2,3,1]
    Output: 4

    Input: nums = [2,7,9,3,1]
    Output: 12
    METHOD:
    `   - for every house, check the maximum you can rob from the current house plus the house before the PREVIOUS
            and then the PREVIOUS
"""


def rob(nums) -> int:
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(rob1 + n, rob2)
        # update rob1 to equal rob2 and rob2 to equal sum at n
        rob1 = rob2
        rob2 = temp

    return rob2


""" Question: House Robber 2
    You're a robber and wants to rob houses but you can't rob adjacent houses, what it is the maximum you can rob
    from that night? NOTE: the last house is connected to the first. CYCLIC
    Input: nums = [1,2,3,1]
    Output: 3

    Input: nums = [2,7,9,3,1]
    Output: 11
    METHOD: 
    `   - Since the house are cyclic, you need to calculate the maximum 
        1. Exclude the first
        2. Exclude the last 
        3. Consider if there was only one house given
"""


def rob(self, nums) -> int:
    return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])


def helper(self, nums):
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


"""Question: House Robber 3 
    The thief has found himself a new place for his thievery again. There is only one 
    entrance to this area, called root. 
    
    Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all 
    houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were 
    broken into on the same night. 
    
    Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
                    3.
                  /   \
                 2     3
                  \      \
                   3.    1.      --> [3,3,1] --> 7 ( Because you can't rob 2 adjancent nodes)
    METHOD: 
     case 1: If we decide to INCLUDE THE ROOT, it will affect how we rob the others
     case 2: If we decide to NOT INCLUDE THE ROOT
                cases = [withRoot, withoutRoot]
        Run DFS - post order traversal , treating each node as a root 
         # return pair: [withRoot, withoutRoot]
"""


def rob(root) -> int:
    def dfs(root):
        if root is None:
            return [0, 0]

        leftPair = dfs(root.left)
        rightPair = dfs(root.right)

        # if a node is the root, that means i need to consider the others without root
        withRoot = root.val + leftPair[1] + rightPair[1]

        withoutRoot = max(leftPair) + max(rightPair)

        return [withRoot, withoutRoot]

    return max(dfs(root))
