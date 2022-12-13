"""" Question 1 - Find Closest Value in BST
    Given a value , transverse the BST to find the value that is closest to it
    METHOD 1: # Average: 0(logn) time | 0(1) space
                    # Worst: 0(n) time | 0(1) space   - in case where the tree is skewed/degenerate
    METHOD 2: # Average: 0(logn) time | 0(logn) space
                    # Worst: 0(n) time | 0(n) space
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
    #   Iteratively
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value

        # decide which way to go
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            return closest
    return closest


def findClosestValueInBstHelper(tree, target, closest):
    #   Recursively
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    # decide which way to go
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        # if the target is exactly the tree value. There will never be another closest
        return closest


""" Question 2 - BST Construction
    Create  a binary search Tree class that
    - insert
    - remove
    - contains/search for values
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: 0(logn) time | 0(1) space
    # Worst: 0(n) time | 0(1) space
    def insert(self, value):
        # Keep drilling down, until a node is None, so you can insert the new node
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average: 0(logn) time | 0(1) space
    # Worst: 0(n) time | 0(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                # we found the value
                return True
        return False

    # Average: 0(logn) time | 0(1) space
    # Worst: 0(n) time | 0(1) space
    def remove(self, value, parentNode=None):
        """
        The idea behind removal is replace node with the right-most
        left value, but keep track of the parentNode before the node to remove
        - First, is to find the value
        - Replace it
        """

        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # we found the value node to remove
                # 1. Does the node have left and right decendants ?
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(
                        currentNode.value, currentNode
                    )  # Go and remove it from the bottom

                # 2. Is the found node the first, i.e does not have a parent node?
                elif parentNode is None:
                    # Asssuming there a child nodes
                    # Like always, replace it with the minimum node from the left.
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    # There wasn't a left child node, we need to take it from the right
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    # This means, there are no left and right node; It's a single tree; DO NOTHING
                    else:
                        pass

                # 3. Ok great!, we found the currentNode to remove & it has a parentNode but it might be that
                # the currentNode doesn't have a left node, that means we need to look to the right child
                elif parentNode.left == currentNode:
                    parentNode.left = (
                        currentNode.left if currentNode.left else currentNode.right
                    )

                # 4. Ok great!, we found the currentNode to remove & it has a parentNode but it was at the right
                # side of the parentNode
                elif parentNode.right == currentNode:
                    parentNode.right = (
                        currentNode.left if currentNode.left else currentNode.right
                    )

                break

        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


""" Question 3 - Validate BST 
    Validate if BST is valid, return True or False. A node a is valid if its child node is None or its strictly 
    greater than the values to the left and less than or equal to the values to the right
                                10
                              /    \
                             5       15
                            /  \      /  \
                           2     5   13  22
                          /            \
                         1            14
    METHOD 1: # 0(n) time | 0(d) space. d is the longest depth of the tree.
        - Just check if the previous element is greater/equal than the next 
         (Same with flatterning a tree into singly linked list)
"""


def validateBst(tree):
    output = inOrderTraversal(tree, [])
    for i in range(1, len(output)):
        if output[i - 1] >= output[i]: # so
            return False
    return True


def inOrderTraversal(tree, array):
    if tree is not None:
        inOrderTraversal(tree.left, array)
        array.append(tree.value)
        inOrderTraversal(tree.right, array)
    return array


""" Question 4 : BST Travesal 
    Traverse a Tree using the 3 order and append all elements into an array:
    METHOD: # 0(n) time | 0(n) space
"""


def inOrderTraverse(tree, array):
    # 0(n) time | 0(n) space
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    # 0(n) time | 0(n) space
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # 0(n) time | 0(n) space
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


""" Question 5 : Construct Minimum height BST 
    Write a function that takes in a SORTED array of distinct intergers, construct a BST, such that the function should
    minimize the height. 
    NOTE: One way to minimize the height of a tree is to avoid skewed cases, fill each level with left & right nodes 
    (Balanced Tree)
    METHOD: 0(n) time | 0(n) space
        Since the array is sorted, we can start from middle as the root node and expand left and right
        for the left & right nodes respectively.
"""


def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array) - 1)


def constructMinHeightBST(array, startIdx, endIdx):
    if startIdx > endIdx:
        return None

    midIdx = startIdx + (endIdx - startIdx) // 2
    bst = BST(array[midIdx])  # Insert the middle Node every time.
    bst.left = constructMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBST(array, midIdx + 1, endIdx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


""" Question 6 : Find the kth Largest value in BST 
    Write a func that takes in a BST and a positive interger (k) and return the kth largest integer contained in the BST
    METHOD 1: 0(n) time | 0(n) space
        Inorder traverse the BST, Save the values in an array and get the kth index value of the largest
    METHOD 2: 0(h + k) time | 0(h) space - h= height of tree,
        The idea is that we want to drill down to the right-most existing node
        While going downwards, save all the nodes you traversed
        From the previously saved nodes, start checking the right and then the left
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    #    0(n) time | 0(n) space
    array = findKthLargestValueInBstHelper(tree, [])
    # array.sort() -- No need to sort because its an inorder travesal where the right values were collected last
    return array[-k]


def findKthLargestValueInBstHelper(tree, array):
    # In order travesal
    if tree is not None:
        findKthLargestValueInBstHelper(tree.left, array)
        array.append(tree.value)
        findKthLargestValueInBstHelper(tree.right, array)
    return array


def findKthLargestValueInBst(tree, k):
    #  0(h + k) time | 0(h) space,  h= height of tree
    recentlyTraversedNodes = []
    count = 1  # because we'll be at the last node to the right

    while tree or recentlyTraversedNodes:
        # if we've not gotten to the last node yet, keep going
        # or if we're looking at the left of the last node
        if tree is not None:
            recentlyTraversedNodes.append(tree)
            tree = tree.right
        # Oh, we've reached the end
        else:
            tree = recentlyTraversedNodes.pop()
            if count == k:
                return tree.value
            count += 1

            # Now check the left
            tree = tree.left


""" Question 7 : Reconstruct a BST 
    Write a func to reconstruct a BST that it's values was previously transerved (Pre-order) into an array.
    Return the root node
    e.g: preOrderTraversalValues=[10, 4, 2, 1, 5, 17, 19, 18] --> 
                10
               /  \
              4    17
             / \     \
            2   5     19
           /          /
          1          18
    RECALL : Pre-order, is ROOT/CURRENT => LEFT => RIGHT
    METHOD 1: 0(n) time | 0(n) space
        Start with root node, 
        save all values that are less than the root node to left array, if not not save to right array
        Build the left and right of the current node recursively
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # start with the root node
    root = BST(preOrderTraversalValues[0])

    left_values = []
    right_values = []
    for num in preOrderTraversalValues[1:]:
        if num < root.value:
            left_values.append(num)
        else:
            right_values.append(num)

    if left_values:
        root.left = reconstructBst(left_values)
    if right_values:
        root.right = reconstructBst(right_values)

    return root


""" Question 8: Same BSTs
    Given an array that was obtained from a BST, from left to right. Write a func that takes two arrays of intergers
    and determine whether these arrays represent the same BST. 
    NOTE: You're not allowed to construct any BST 
    e.g : arrayOne=[10, 15, 8, 12, 94, 81, 5, 2, 11], arrayTwo=[10, 8, 5, 15, 2, 12, 11, 94, 81] --> 
    true // both arrays represent the BST below
                    10
                   /  \
                  8    15
                 /     / \
                12    12  94
               /     /    /
              2     11   81
    METHOD 1: 0(n1 + n2) time | 0(n1 + n2) space
        - Same BSTs have to have the same root node, that's how you compare
        - Contineously split the arrays into 2s. One that is less than the current node and the other that is greater 
"""


def sameBsts(arrayOne, arrayTwo):
    # if the nodes were both empty/ You've traversed to the end
    if len(arrayOne) == len(arrayTwo) and len(arrayOne) == 0:
        return True

    # if they're a single node/leaf and both equal return True
    if len(arrayOne) == 1 and len(arrayTwo) == 1 and arrayOne[0] == arrayTwo[0]:
        return True

    # Is the root node similar and of equal length?
    if arrayOne[0] == arrayTwo[0] and len(arrayOne) == len(arrayTwo):
        arrayOneRoot = arrayOne.pop(0)
        arrayTwoRoot = arrayTwo.pop(0)

        newArrayOneLeft = [value for value in arrayOne if value < arrayOneRoot]
        newArrayOneRight = [value for value in arrayOne if value >= arrayOneRoot]

        newArrayTwoLeft = [value for value in arrayTwo if value < arrayTwoRoot]
        newArrayTwoRight = [value for value in arrayTwo if value >= arrayTwoRoot]

        return sameBsts(newArrayOneLeft, newArrayTwoLeft) and sameBsts(
            newArrayOneRight, newArrayTwoRight
        )
    else:
        return False


""" Question 9: Validate 3 nodes 
    Given 3 nodes in a BST, nodeOne, nodeTwo, nodeThree, validate :
    - if nodeOne is a parent of nodeTwo and nodeThree a decendant of nodeTwo
            OR
    - if nodeThree is a parent of nodeTwo and nodeOne a decendant of nodeTwo
    e.g : nodeOne =  10, nodeTwo = 8, nodeThree = 2  --> True

                    10
                   /  \
                  8    15
                 /     / \
                12   13  94
               /     /    /
              2     11   81
    METHOD 1: 0(d) time | 0(1) space
            - consider nodeOne as parentNode, check if nodeTwo can be found first and the proceed to find nodeThree
            - Repeat, by considering nodeThree as parentNode
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    one = nodeOne
    isTwoFoundInOne = False

    while one:
        if one and isTwoFoundInOne is False:
            # Lets search for nodeTwo
            if one.value == nodeTwo.value:
                isTwoFoundInOne = True
            elif one.value < nodeTwo.value:
                one = one.right
            else:
                one = one.left
        else:
            # nodeTwo has been found in One, so search for Three
            if one.value == nodeThree.value:
                return True
            elif one.value < nodeThree.value:
                one = one.right
            else:
                one = one.left

    three = nodeThree
    isTwoFoundInThree = False

    while three:
        if three and isTwoFoundInThree is False:
            # Lets search for nodeTwo
            if three.value == nodeTwo.value:
                isTwoFoundInThree = True
            elif three.value < nodeTwo.value:
                three = three.right
            else:
                three = three.left
        else:
            # nodeTwo has been found in Three, so search for One
            if three.value == nodeOne.value:
                return True
            elif three.value < nodeOne.value:
                three = three.right
            else:
                three = three.left

    return False


""" Question 10: Right smaller than 
    Given an array that takes in an array of integers, return an array of the same length where each element
    in the output array correspond to the number of intergers in the input array that are to the right and 
    strictly smaller than the current integer from the input array
    e.g : array=[8, 5, 11, -1, 3, 4, 2] --> output=[5, 4, 4, 0, 1, 1, 0]
    METHOD 1: 0(n^2) time | 0(n) space
    METHOD 2: 
"""


def rightSmallerThan(array):
    output = []
    for i in range(len(array)):
        countValidNumbers = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                countValidNumbers += 1
        output.append(countValidNumbers)
    return output
