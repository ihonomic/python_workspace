""" Question 1 - Branch sums
    Write a func that takes in a BT and returns the total sum of its branches (from leftmost to rightmost)
    e.g:                        1
                                /  \
                              2     3
                            /  \   / \
                         4      5 6  7
                        / \    /
                       8  9  10                       --> [15, 16,18, 10, 11]
    // 15: 1+2+4+8
    // 16: 1+2+4+9
    // 18:  1+2+5+10
    // 10:  1+3+6
    // 11:  1+3+7
    Method: 0(n) time | 0(n) space
    - Use a deque, to save the node and running sum, insert the left node last. So that it becomes the first
    to pop out. Also consider passing down the running sum until a leaf node is found
"""


def branchSums(root):
    queue = [(root, 0)]
    sumsOfBranch = []
    while queue:
        currentNode, runningSum = queue.pop()
        if currentNode is not None:
            runningSum += currentNode.value
            # NOTE: consider the right side first
            queue.append((currentNode.right, runningSum))
            queue.append((currentNode.left, runningSum))

            # Have we reach the leaf node
            if currentNode.left is None and currentNode.right is None:
                sumsOfBranch.append(runningSum)

    return sumsOfBranch


""" Question 2 - Node depths
    Write a func that takes in a BT and returns the sum of its node depth. 
    NOTE: Depth is the distance between a node and its root
    e.g:            Tree =  1
                               /  \
                             2     3
                           /  \   /  \
                         4    5  6   7
                        / \
                      8    9                      --> 16
    // 2 & 3 has a depths of 1 each   -- 2 * 1
    // 4, 5, 6 & 7 has depths of 2 each --4 *2 
    // 8 & 9 has depths of 3 each   -- 2*3
    Method: 0(n) time | 0(h) space
    - Use a deque, to save the nodes and depths, 
    - If a node is valid(not None), append the left and right to queue and increment depth by 1
"""


def nodeDepths(root):
    totalDepth = 0
    queue = [(root, 0)]
    while queue:
        currentNode, depth = queue.pop()
        if currentNode is not None:
            totalDepth += depth
            # the appending order doesn't matter
            queue.append((currentNode.left, depth + 1))
            queue.append((currentNode.right, depth + 1))

    return totalDepth


""" Question 3 - Invert Binary Tree
    Write a func that takes in a BT and inverts it. That is, it should swap left and rightnodes ( childnodes of parent)
    e.g:                        tree = 1
                                         /  \
                                       2      3
                                     /   \   /  \
                                   4     5  6    7 
                                  /  \
                                 8   9
                                 -->                                1
                                                                   /    \
                                                                 3        2
                                                               /  \      /  \
                                                             7     6   5     4
                                                                              /  \
                                                                            9     8
    Method 1: 0(n) time | 0(n) space
    Method 2: 0(n) time | 0(d) space
"""


def invertBinaryTree(tree):
    # 0(n) time | 0(n) space
    queue = [tree]
    while queue:
        node = queue.pop(0)
        if node is not None:
            swapLeftAndRight(node)
            queue.append(node.left)
            queue.append(node.right)


def invertBinaryTree(tree):
    # 0(n) time | 0(d) space
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapLeftAndRight(node):
    node.left, node.right = node.right, node.left


""" Question 4 - Binary Tree Diameter 
    Write a func that takes in a BT and return its diameter. The diameter is defined as the length of its 
    longest path, even if the path doesn't pass through the root of the tree.
    
    A path is a collection of nodes where each node is not connected to more than 2 nodes. The length of the path
    is the number of edges between the path's first node and it's last node.
    
    # The Diameter of a tree is defined as the longest path, (edges) without
    # interruption
    e.g:                                        1
                                                /  \
                                              3     2
                                            /  \
                                          7    4
                                        /         \
                                      8            5
                                     /               \
                                    9                 6
                                    ---> 6
            // There are 6 edges between the first node and the last node of this tree's longest path.
    Method: 0(n) time 0(h) space
"""

""" Question 5 - Find Successor
    Write a func that takes in a BT (where nodes have an additional pointer to their parent node) 
    and a node contained in the tree, return the given node successor.
    
    A node successor is the next node to be visited immediately after the given node when traversing its tree 
    using inOrder traversal technique. NOTE: A node has no successor if its the last node to be visited in the inOrder 
    travesal
    e.g:                    tree =   1
                                       /  \
                                     2     3
                                  /   \
                                4      5
                             /
                           6                           node = 5   --> 1
    // Using inorder technique 6-4-2-5-1-3 // return 1 because it comes immediately after 5.
    Method: 0(n) time | 0(n) space
    Method 2: 0(h) time | 0(1) space
"""


def findSuccessor(tree, node):
    # 0(n) time | 0(n) space
    inOrderArray = InOrderTraversal(tree, [])

    # find the next node after the given node. (successor)
    for idx in range(len(inOrderArray)):
        if inOrderArray[idx] == node:
            # if the node is found but its at the last, return None
            if idx == len(inOrderArray) - 1:
                return None

            return inOrderArray[idx + 1]


def InOrderTraversal(node, array):
    if node is not None:
        InOrderTraversal(node.left, array)
        array.append(node)
        InOrderTraversal(node.right, array)
    return array


""" Question 6 - Height balanced binary Tree
    Given the root node of a BT. Write a func to return True if it is balanced else False.
    A tree is balanced if the difference btw the height of its left subtree & height of its right subtree is at most 1
    e.g:                        tree = 1
                                        /   \
                                      2      3
                                    / \        \
                                  4    5       6
                                      /  \
                                    7     8   --> True
    Method: 0(n) time | 0(h) space
"""

""" Question 7 - Max Path sum In Binary Tree
    Write a function that takes in a Binary Tree and return its max path sum.
    NOTE: A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes;
    a path sum is the sum of the nodes in a particular path
                        tree =  1
                               /     \
                             2        3
                           /  \      /  \
                         4     5   6    7  --> 18  (5 + 2 + 1 + 3 + 7)
    Method: 0(n) time | 0(logn) space
        - Be careful of negative values. Take the max btw left, right & zero(0)
        - This will imply, Just incase the child sum path is negative, don't consider it
        - Start by considering each node as a path
        - But why start from the root node when you can just solve the smaller problems first
        - Remember, the outcome of the sub-nodes can not be returned to the parent because
        - in some cases, the sub-nodes have multiple paths (splits)
        - Instead, return to parent the maximum btw left & right path, Do not split
"""


def maxPathSum(tree):
    res = [tree.value]

    # Return max path sum without spilting
    def dfs(tree):
        if not tree:
            return 0

        leftMax = dfs(tree.left)
        rightMax = dfs(tree.right)

        # Just incase the subpath sum is negatives, we want to end the change at the current node
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # Compute path sum with split
        splitSum = tree.value + leftMax + rightMax

        # Update result
        res[0] = max(res[0], splitSum)

        return tree.value + max(leftMax, rightMax)

    dfs(tree)
    return res[0]


""" Question 8 - Find Nodes Distance K 
    Given the root node of a binary Tree, a target value of a node in a tree, k a positive Integer.
    Write a function that returns the values of all the nodes that are exactly distance k from the node with target
     value.
     e.g: tree = 1
          / \
         2   3
        / \   \
       4   5   6
              /  \
             7    8
   target = 3
    k = 2           --> [2,7,8]
     NOTE: The distance btw two nodes is the number of edges that must be traversed to go from one node to the other.
     For example, right & left child node of a parent has a distance 1 from each other.
    METHOD: 0(n) time | 0(n) space
     - Use a hashMap to hold each parentNodes 
    parents ={1:None, 2:Node(1), 3:Node(1)}
    - DFS to find the target node from the parentNodes, it will be at left or right
    - Create a queue to store (node, distance), starts with (targetNode, distance=0)
    - Add to the queue, the target neigbours (left, right, parents) and their distance
    - From the last node saved in the queue, pop it out and use it to compute subsequent nodes
    - Keep a track of nodes you've already added, so that u don't re-added them to the queue
    - You can stop the proces if the last pop out node from the queue has a distance k. 
    - Because, this is a BFS, that means other element left in the queue also has a distance k from target, 
    return ALL
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)

    return breathFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)


def breathFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
    # We can use python deque
    # we store the node and the distances from the target node, if it's
    # equal to k, return the values of the currentNode and the nodes left in the queue
    # But take not, we've to mark nodes that have already been on the queue
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0)

        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK

        # Take all the neigboring nodes and add to queue, if they've not been on queue before
        connectedNodes = [
            currentNode.left,
            currentNode.right,
            nodesToParents[currentNode.value],
        ]
        for node in connectedNodes:
            if node is None:
                continue

            if node.value in seen:
                continue

            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))  # Increase the distance by 1

    return []


def getNodeFromValue(value, tree, nodesToParents):
    # just incase the target node is root
    if tree.value == value:
        return tree

    targetParent = nodesToParents[value]
    if targetParent.left is not None and targetParent.left.value == value:
        return targetParent.left

    return targetParent.right


def populateNodesToParents(node, nodesToParents, parent=None):
    if node is not None:
        nodesToParents[node.value] = parent
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)


""" Question 9 - InOrder Traversal Iteratively.
    Just like the recursive inOrder travesal, do it iteratively. 
    NOTE: Each node has a parent pointer to their parent nodes. For this question, you'll be given a callback function, 
    as an argument that should be called on each node. 
    METHOD : 0(n) time | 0(1) space. Unlike the recursive: that is 0(n) space 
       - The idea, Keep track of the previous Node, cause that would help us go back.
        1) PROGRESS DOWNWARDS: If previousNode is None, or if previousNode is the currentNode parent,
            Keep going far left, if there is left, otherwise callback on the currentNode, either go right or go back
        2) Incases where, previousNode is now the currentNode left, that means, we're moving
            back up
        3) previousNode can be None, so go back
        Anytime, we exhaust a node, we need to callback and then go back up
"""


def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree
    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = (
                    currentNode.right if currentNode.right else currentNode.parent
                )
        elif previousNode == currentNode.left:
            # we've gone backup, previous node is now at downwards left
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right else currentNode.parent
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode


""" Question 10: Fattern Binary Search 
    Write a function that takes in a binary tree, flatterns it and return its left-most node
    HACK: If its a binary Tree, flatterning it will return the sorted order
    e.g:  tree = 1
          /  \
         2    3
        /  \  /
       4    5 6
           / \
          7   8    --> 4-2-7-5-8-1-6-3 // --> 4
    METHOD : 0(n) time | 0(n) space
        - Perform an Inorder travesal, then correct each node in the array, return the new root(leftmost node)
"""


def flattenBinaryTree(root):
    inOrderNodes = inOrderTraverse(root, [])
    # connect the nodes
    for i in range(len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNodes[0]


def inOrderTraverse(root, array):
    if root is not None:
        inOrderTraverse(root.left, array)
        array.append(root)  # in this case we want the node, not the value(root.value)
        inOrderTraverse(root.right, array)
    return array


"""Question: Flatten Multilevel Linked List 
    https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
    Imagine a linked list with not just a next node, but a down node as well. 
    We want to write a function that would "Flatten" that linked list by taking all the downward segments and merging 
    them up between their parent and their parent's next. 
    e.g:
    [1] -> [2] -> [3] -> [8] -> [10]
               |      |
	           |     [9]
			   |
			  [4] -> [5] -> [6]
			                 |
							[7]
							--> 
	[1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9] -> [10]
	METHOD:
	    Recursively save to a stack, the current node, the downward node, the the next node
	
"""


class Node:
    def __init__(self, value: int, next=None, down=None):
        self.value = value
        self.next = next
        self.down = down


chain = Node(
    1,
    Node(
        2, Node(3, Node(8, Node(10), Node(9)), Node(4, Node(5, Node(6, down=Node(7)))))
    ),
)


def flatten_chain(chain):
    def traverse(node, array):
        if node is not None:
            array.append(node)
            traverse(node.next, array)
            traverse(node.down, array)
        return array

    arrayOfNodes = traverse(chain, [])

    # connect the nodes
    for i in range(len(arrayOfNodes) - 1):
        leftNode = arrayOfNodes[i]
        rightNode = arrayOfNodes[i + 1]
        leftNode.next = rightNode

    # end the last node in the linkedlist
    lastNode = arrayOfNodes[i + 1]
    lastNode.next = None
    return arrayOfNodes[0]


""" Question 11: Right Sibling Tree 
    Write a function that takes in a binary Tree, transforms it (in-place) into a right sibling tree, and return its root
    A RIGHT SIBLING TREE-> Is when you make every node right pointer to point to it's right sibling instead of its right 
    child. NOTE: A node right sibling is the node immediately to its right, or None.
    e.g:  
                    tree =    1
                            /    \
                           2      3
                          / \    /  \
                        4    5  6    7
                       / \    \ /    / \
                      8   9  10 11  12  13
                                /
                               14 
                            -->

                            1
                           /
                          2 ------------3
                         /             /
                        4-----5-------6----7
                       /              /    /
                      8---9         10-11 12-13    # the node with the value 10 no longer has a node pointer
                                       /
                                      14
    METHOD : 0(n) time | 0(d) space
       - Save each node in a queue.
       - from the last saved, is at the same level with the next, connect the right pointer to it, else
        point it to None
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    queue = [(root, 0)]
    while len(queue) > 0:
        node, level = queue.pop(0)

        if node is None:
            continue

        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))

        nextNode = queue[0]  # time to change the pointer of the firstNode
        # if they're of the same level, connect them, else point to None
        if level == nextNode[1]:
            node.right = nextNode[0]
        else:
            node.right = None
    return root


""" Question 12: All kinds of Node depths
    Write a function that takes in a binary Tree and returns the sum of all its subtrees nodes depths
    NOTE: The distance btw a node and it's tree root is called a node depth.(level * distance)
    e.g:          1 d=16
                   / \
          d=6   2   3    d = 2 
                 / \  / \
         d=2  4   5 6  7
               / \
              8   9     
                        ( 8 & 9 are on level 3, => 3 * 2(nodes) = 6, 
                         4,5,6, & 7 are on level 2, => 2 * 4(nodes) = 8,
                         2 & 3 are on level 1, => 1 * 2(nodes) = 2
                            --> 16
    METHOD 1 : 0(n) time | 0(h) space
        - Consider each node as a new root
        - Divide the next level depth by 2
    METHOD 2 : 0(n) time | 0(d) space
        - Each node of depth D adds sum([1, D]) to the final result, 
        - Considering one level higher  
"""


def allKindsOfNodeDepths(root):
    # 0(n) time | 0(h) space
    res = 0
    stack = [(root, 0)]
    while len(stack) > 0:
        node, depth = stack.pop()
        if node is None:
            continue
        res += depth * (depth + 1) / 2
        stack.append((node.left, depth + 1))
        stack.append((node.right, depth + 1))
    return res


def allKindsOfNodeDepths(root, depth=0):
    # 0(n) time | 0(d) space
    if not root:
        return 0
    total = sum(range(1, depth + 1))
    total += allKindsOfNodeDepths(root.left, depth + 1)
    total += allKindsOfNodeDepths(root.right, depth + 1)
    return total


""" Question 13: Compare tree traversal
    Write a function that takes in the root nodes of 2 binary trees and returns a boolean whether their leaf
    travesal are the same.(NOTE: leaf nodes are nodes without left or right). If both BT has leaf nodes in the same other 
    return True.
    e.g: 
    tree1 = 1
               / \
              2   3
             / \   \
            4   7   5
                   / \
                  8   6

    tree2 = 1
               / \
              2   3
             / \   \
            4   5   6
               / \
              7   8
                              --> True [4,7,8,6]
    Method 1: 0(n) time | 0(h1 + h2) space
        - For the 2 trees, Get all the leafs nodes into an array and compare them
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal(tree1, tree2):
    leaves1 = getLeavesNodes(tree1, [])
    leaves2 = getLeavesNodes(tree2, [])

    return leaves1 == leaves2


def getLeavesNodes(node, array):
    if node is None:
        return

        # Pre-order travesal
    if node.left is None and node.right is None:
        array.append(node.value)

    if node is not None:
        getLeavesNodes(node.left, array)
        getLeavesNodes(node.right, array)

    return array


""" Question 14: Symmetrical Tree 
    Write a function that takes a binary Tree, and returns True if the tree is symmetrical. A tree is symmetrical 
    if the left and right subtrees are mirror images of each other 
    e.g: 
    tree =        1
               /    \
              2      2
             / \    / \
            3   4  4   3
           / \        / \
          5  6       6   5        
                            --> True 
    Method 1: 0(n) time | 0(h) space
        - 
    Method 2: 0(n) time | 0(h) space
        - 
"""
# Method 1 
def symmetricalTree(tree):
    return isMirrored(tree.left, tree.right)


def isMirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return isMirrored(left.left, right.right) and isMirrored(left.right, right.left)

    return left == right 

# Method 2 
def symmetricalTree(tree):
    queueLeft = [tree.left]
    queueRight = [tree.right]

    while len(queueLeft) > 0:
        left = queueLeft.pop()
        right = queueRight.pop()

        if left is None and right is None:
            continue 

        if left is None or right is None or left.value != right.value:
            return False 

        queueLeft.append(left.left)
        queueLeft.append(left.right)
        
        queueRight.append(right.right)
        queueRight.append(right.left)

    return True 
        
""" Question 15: Merge Binary Tree 
   Given 2 Binary Tree, merge them and return the resulting tree. If two nodes overlap during the merger
   then sum the values, otherwise use the exiting node 

   Note: Your solution can either mutate the exiting tree or return a new tree 
    e.g: 
    tree1 =      1
               /  \
              3    2
             / \    
            7   4  

    tree2 =       1
               /    \
              5      9
             /      / \
            2      7   6
      
                            ----> 

                 2
               /  \
              8    11
             / \   / \ 
            9   4 7   6

    Method 1: 0(n) time | 0(h) space   - 
    - Add node Two value to node One, if nodeOne becomes empty, link nodeTwo subtree to it. 
    - Keep track of the next left and right in a queue/OR stack
"""

def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2 
        
    queueOne = [tree1]
    queueTwo = [tree2]

    while len(queueOne) > 0:
        nodeOne =  queueOne.pop() 
        nodeTwo =  queueTwo.pop() 

        if nodeTwo is None:
            continue 

        nodeOne.value += nodeTwo.value 

        if nodeOne.left is None:
            nodeOne.left = nodeTwo.left 
        else:
            queueOne.append(nodeOne.left)
            queueTwo.append(nodeTwo.left)
            
        if nodeOne.right is None:
            nodeOne.right = nodeTwo.right 
        else:
            queueOne.append(nodeOne.right)
            queueTwo.append(nodeTwo.right)

    return tree1 
        
        
        
""" Question 16: Split Binary Tree 
   Write a func that takes a binary Tree, with at least one node and check if that tree can be split into two
   binary Tree of equal sum by removing a single edge. If this split is possible, return the new sum of each binary Tree, 
   otherwise return 0. NOTE: You dont need to return the edge that was removed. 

   The sum of a binary tree is the sum of all values in that binary Tree. 
    e.g: 
    tree =       1
               /   \
              3    -2
             / \   / \
            6  -5 5   2
           /
          2  
                            ----> 6 // Remove the edge to the left, that links 3 & 1, both splitted tree has sum of 6. 


    Method 1: 0(n) time | 0(h) space   - 
    - The idea is to find the desired sum that makes both trees equal when we split
     First we find the total sum of the root tree, half of it is our desired sum, 

    - Next, We need to go through every node to check if we find this desired sum downwards
     while neglecting the parent sum 
     NOTE: if we dont find the desired sum, return 0 

     Starting from the bottom 
     sum(currentNode) = currentNode.value + sum(currentNode.left.value) + sum(currentNode.right.value)
"""

def splitBinaryTree(tree):
    desiredSum = getTreeSum(tree) / 2

    # Drill downwards to the leaf nodes and check if the currentNode and the sum of its children equals desired sum, 
    # if yes, return (desiredSum, True)
    canBeSplit = trySubTrees(tree, desiredSum)[1]

    # If can be split is True, return our calculated desired sum
    return desiredSum if canBeSplit else 0


def trySubTrees(tree, desiredSum):
    if tree is None:
        return (0, False)  # (currentSum, Can be split at leaf?)

    leftSum, leftCanBeSplit = trySubTrees(tree.left, desiredSum)
    rightSum, rightCanBeSplit = trySubTrees(tree.right, desiredSum)

    currentSum = tree.value + leftSum + rightSum 
    canBeSplit = leftCanBeSplit or rightCanBeSplit or currentSum == desiredSum
    return (currentSum, canBeSplit)

def getTreeSum(tree):
    if tree is None:
        return 0 
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)

""" Question 17: Evaluate Expression Tree 
    Write a function to evaluate a tree mathematically, resulting in a single interger. 
    All leaf nodes in the tree represents operands which will always be positive numbers, 
    but other nodes represent operators. 
    There are 4 operators supported, each of which is represented by a negative integer. 
     -1 : Addition operator, adding the left & the right subtrees
     -2 : Subtract operator, subtracting the right subtree from the left substree
     -3: Divide operator, dividing the left subtree by the right subtree. round to towards if decimal. 
     -4 : Multiply operator, multiply the left subtree by the right subtree

    You can assume the tree will always be a valid expression tree. Each operator
    also works as a grouping symbol, meaning the bottom of the tree is always evaluated 
    first, regardless of the operator
    e.g: 
    tree =      -1
               /   \
             -2    -3
             / \   / \
           -4   2 8   3
           / \
          2   3      


                              --> 6 (((2 * 3) - 2) + (8 / 3))
    Method: 0(n) time | 0(h) space
    Recursively drilling down to the leaf node 
    Perform the operand and operator calculations and return to previous 
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # If we're at leaf node
    if tree.value >= 0:
        return tree.value

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue / rightValue)
    if tree.value == -4:
        return leftValue * rightValue


""" Question 18: Binary Tree Diameter
    Write a function that takes in a binary tree and return it's diameter. The diameter is the
    length of its longest path, even if the path doesnt pass through the root of the tree. 

    A path is a collection of connected nodes in the tree, where no node is connected to more 
    than two other nodes. The length of a path is the number of edges betw the paths first node 
    and its last node. 
    e.g: 
    tree =       1
               /  \
              3    2
            /  \  
           7    4
         /       \
        8         5
      /            \
     9              6


     --> 6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6 
    Method: 
        Go down to the leaf node and calculate the depth upwards, add the depths from 
        both right and left to determine the current depth (path)

        In the example above, leaf nodes 9 & 6 have depths of 3 each, adding both equals 6
"""


def binaryTreeDiameter(tree):
    longestPath = [0]  # recurse down values for a possible change
    calculateLongestPath(tree, longestPath)
    return longestPath[0]


def calculateLongestPath(root, longestPath):
    # The idea is that we're looking for the longest path while using
    # recursion to find the longest depth of the left subtree and of the
    # right subtree

    if root is None:
        return 0

    leftDepth = calculateLongestPath(root.left, longestPath)
    rightDepth = calculateLongestPath(root.right, longestPath)

    currentLongestPath = leftDepth + rightDepth
    longestPath[0] = max(longestPath[0], currentLongestPath)

    return max(leftDepth, rightDepth) + 1
