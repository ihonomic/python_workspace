"""
GRAPHS - Vertices are nodes (v), Edges are connected lines between nodes (e)
"""

""" Question 1: Depth - first search
    Given a node class that has a name and an array of optional children nodes.
    Implement a DFS method on the node class, which takes in an empty array, traverses the tree
    using DFS approach (moving from left to right), stores all the nodes in the input array and return it
    e.g:                            A
                                  /  |  \
                                B    C   D
                              /  \       /  \
                            E     F    G    H
                                /   \    \
                              I       J    K     --> [A, B, E, F, I, J, C, D, G, K, H]
    Method: 0(v + e) time | 0(v) space 
        Add the current item, call the function on the item's children, return the array.
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Add the current item, call the function on the item's children, return the array.
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


""" Question 2: Single cycle check
    Given an array of Integers representing a jump distance. E.G +2 means jump forward twice, 
    and -2 means jumps backward twice. NOTE: Jumps can wrap around the array.
    Write a func that returns a boolean wether the jumps in an array represents a single cycle.
    
    A single cycle occurs if starting at any index, EVERY ELEMENT IS VISITED ONLY ONCE. 
    (Where the first jump stops, continue from there. )
    e.g:   [2,3,1,-4,-4,2] --> True
            [1,-1,1,-1] --> False
    Method: 0(n) time | 0(1) space 
        - Make sure to visit all elements 
        - if we visited n length and we're not back to our starting point, then there's a False. 
        - if we've visited the exact length size of the array, end the loop and check if we're back to the starting index
"""


def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0
    while numElementsVisited < len(array):
        # Return false, if we got back to the starting index prematurely
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        # Jump to the new index
        currentIdx = getNextIdx(currentIdx, array)

    # if we've visited the exact length size of the array, end the loop and check if we're back to the starting index
    return currentIdx == 0


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    # handle negative (reverse jumps)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


""" Question 3: Breath - first search
    Given a node class that has a name and an array of optional children nodes.
    Implement a BFS method on the node class, which takes in an empty array, traverses the tree
    using DFS approach (moving from left to right), stores all the nodes in the input array and return it
    e.g:                            A
                                  /  |  \
                                B    C   D
                              /  \       /  \
                            E     F    G    H
                                /   \    \
                              I       J    K     --> [A, B, C, D,E,F,G,H,I,J,K]
    Method: 0(v + e) time | 0(v) space 
        Use a queue, the explore the earliest node
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


""" Question 4: Rivers Sizes
    Given a 2D array(matrix) of potentially unequal widths and heights containing 0s & 1s. Each
    0s represents land and 1s represent river. NOTE: A river consists of any number of 1s (horizontally, or vetically) 
    but not diagonal. The number of adjacent 1s forming a river determine its size.
    
    NOTE: A river can twist, it doesn;t necessary have to be straight horizontal or vertical. It can be L-shape, for example
    Write a function that returns the sizes of all the rivers in any order.
    e.g:  matrix=[
                    [1, 0, 0, 1, 0], 
                    [1, 0, 1, 0, 0], 
                    [0, 0, 1, 0, 1], 
                    [1, 0, 1, 0, 1], 
                    [1, 0, 1, 1, 0]
                ]    --> [1,2,2,2,5]
    Method: 0(wh) time | 0(wh) space - width and height of the matrix
    - You need to keep track of all the 1s you've seen and which river they're a part of 
    - Whenever you encounter a 1, you'll transverse, either with BFS or DFS all the 1s that are part of it's river
       when you encounter 0 you stop 
    - Remember to keep track of the nodes already visited (adding a True/False flag)
    skip any vertices that's already visited. 
"""


def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]  # Create flags, Mark all as not visited
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    # apply DFS iteratively - stack but if BFS, use a queue
    nodesToExplore = [[i, j]]
    while nodesToExplore:
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        # else mark it as now visited
        visited[i][j] = True
        # Now, don't do anything if land is found
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        # Now start exploring it's neigbours, return their index as an array
        unvisitedNeighbors = getUnvisitedNeigbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    # if a river size was found
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeigbors(i, j, matrix, visited):
    # Beware of outofbounds , TRICK: consider bounds from the middle locations
    unvisitedNeighbors = []

    # 1. TOP. if we've not visited the neigbor above (i.e not on first row)
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])

    # 2. BOTTOM. if we've not visited the neigbor below (i.e not on last row)
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])

    # 3. LEFT.
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])

    # 4. RIGHT
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])

    return unvisitedNeighbors


""" Question 5: Youngest common ancestor
    You're given 3 inputs. All are instances of AncestralTree class with an ancestor property pointing to their youngest
    ancestor in an ancestral Tree (Except the Topmost ancestor points to None) and the other 2 inputs are decendants 
    in the ancestral tree.
    
    Write a function that returns the youngest common ancestor to the two decendants. 
    NOTE: Decendants is considered as it's own ancestor. Therefore from the below example, YCA is A.
                            A
                          /
                        B 
    e.g:        topAncestor = node A 
                  decendantOne = node E
                  decendantTwo = node I 
                                                    A
                                                  /    \    
                                                B       C
                                             /     \   /  \
                                            D      E  F   G
                                          /  \
                                        H     I                               --> node B
    Method 1: 0(d) time | 0(n) space
        For each ancestor in the first descendant, add it to a set until no more ancestor.
        For the second descendant, check if the ancestor exists in the set
    Method 2: 0(d) time | 0(1) space
        Find the depths, fast-track the longest one to be the same depth with the shortest, then compare 
        both.
"""


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # 0(d) time | 0(n) space
    history = set()
    while descendantOne and descendantOne.name is not None:
        history.add(descendantOne.name)
        descendantOne = descendantOne.ancestor

    while descendantTwo and descendantTwo.name is not None:
        if descendantTwo.name in history:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # 0(d) time | 0(1) space
    heightOfOne = findDepth(descendantOne, topAncestor)
    heightOfTwo = findDepth(descendantTwo, topAncestor)

    if heightOfOne > heightOfTwo:
        for _ in range(heightOfOne - heightOfTwo):
            descendantOne = descendantOne.ancestor

    if heightOfTwo > heightOfOne:
        for _ in range(heightOfTwo - heightOfOne):
            descendantTwo = descendantTwo.ancestor

    while descendantOne.name != descendantTwo.name:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


def findDepth(node, top):
    depth = 0
    while node.name != top.name:
        depth += 1
        node = node.ancestor
    return depth


""" Question 6: Remove Islands
    Given a 2D array(matrix) of potentially unequal widths and heights containing 0s & 1s. Each
    0s represents white and 1s represent black. An island is defined as any number of 1s that are horizontally 
    or vertically adjacent (but not diagonal) and that doesn't touch the border of the image. In other words a group 
    of horizontally or vertically 1s isn't an island if any of those 1s are in the first row, last row, last column or first 
    column of the input matrix.
    
    NOTE: An island can twist, i.e have L shape
    
    You can think of an island that doesn't touch the the border of the two-toned image.
    
    Write a function that returns a modified version of the matrix, where all of its island are removed. You remove an island
    by replacing it with 0s. Mutate the original matrix
    
    e.g: matrix=[
                [1, 0, 0, 0, 0, 0], 
                [0, 1, 0, 1, 1, 1], 
                [0, 0, 1, 0, 1, 0], 
                [1, 1, 0, 0, 1, 0], 
                [1, 0, 1, 1, 0, 0], 
                [1, 0, 0, 0, 0, 1]
            ]    --> 
            
            [
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1], 
                [0, 0, 0, 0, 1, 0], 
                [1, 1, 0, 0, 1, 0], 
                [1, 0, 0, 0, 0, 0], 
                [1, 0, 0, 0, 0, 1]
            ]
    Method 1: 0(wh) time | 0(wh) space
        - Create an identical matrix of flags False
        - First find all the 1s at the border and DFS the other 1s connected to them and mark them as True
        - Second: Look in the interior, and swap 1s to 0s if False
    Method 2: 0(wh) time | 0(wh) space
         - Swap all 1s at the border and those connected to it with 2.
        - Now go through the entire matrix and replace the 2s with 1 and the leftover 1s with 0

"""


def removeIslands(matrix):

    onesConnectedToBorder = [[False for value in row] for row in matrix]  # Create flags, Mark all as False

    # 1.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rowIsBorder = i == 0 or i == len(matrix) - 1  # Is the current row first or last?
            colIsBorder = j == 0 or j == len(matrix[i]) - 1  # Is the current col first or last?
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue

            if matrix[i][j] != 1:
                continue

            findOnesConnectedToBorder(matrix, i, j, onesConnectedToBorder)

    # 2.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if onesConnectedToBorder[i][j] is False and matrix[i][j] == 1:
                matrix[i][j] = 0

    return matrix


def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    # apply DFS iteratively - stack but if BFS, use a queue
    stack = [(startRow, startCol)]
    while stack:
        currentRow, currentCol = stack.pop()

        alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
        if alreadyVisited:
            continue

        onesConnectedToBorder[currentRow][currentCol] = True

        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)  # only add to stack if neighbor is 1


def getNeighbors(matrix, row, col):
    # Beware of outofbounds
    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < numRows:  # DOWN
        neighbors.append((row + 1, col))
    if col - 1 >= 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < numCols:  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors













