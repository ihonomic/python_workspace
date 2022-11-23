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
        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
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
                nextNode = currentNode.right if currentNode.right else currentNode.parent
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
    for i in range(len(inOrderNodes)-1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i+1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNodes[0]


def inOrderTraverse(root, array):
    if root is not None:
        inOrderTraverse(root.left, array)
        array.append(root)  # in this case we want the node, not the value(root.value)
        inOrderTraverse(root.right, array)
    return array


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
