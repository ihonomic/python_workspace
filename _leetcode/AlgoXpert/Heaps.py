""" Question 1 - Min Heap construction
    NOTE: Heap is a complete binary tree. All it's level are equal . Its represented as an array
    For a min-heap, the peak element is the smallest value but for a max-heap, it is the largest.

    - currentNode = i
    - childOne = 2i + 1
    - childTwo = 2i + 2
    - parentNode = (i-1) // 2

    SiftUp - When an element is (inserted) to the heap.
            Comparing the current inserted node with it's parent node until it is in its right position
            ( compare to its parent)
            0(logn) time
    SiftDown - Usually, After the smallest/largest has been pop off ( remove)
            Before the value is removed, it is swapped with the last element and then pop off.
            But this step will imply that the new node at first Index, is out of order. So to correct this,
            We siftDown.
            For min-Heap, This is the act of contineously replacing the smallest child node with the first index
            node until it is in its rightful position.
            ( compare to both childs)
             0(logn) time
    BuildHeap -
            Makes use of the siftDown method


    Implement a MinHeap class that does the following:
    - Build a min heap from an array of integers
    - Inserting intergers in the heap
    - Removing heap minimum intergr/ root value
    - Peeking heap minimum / root value
    - shifting intergers up and down the heap, which is to be used when inserting and removing values

"""


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # 0(n) time
    def buildHeap(self, array):
        # get the first parentIdx by obtaining the last parent, and then reverse it
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array

    # 0(logn) time
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # 0(logn) time
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[parentIdx] > heap[currentIdx]:
            self.swap(parentIdx, currentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        # Removing means to swap the first & last and then pop off, but siftDown to position
        # the first element
        self.swap(0, len(self.heap) - 1, self.heap)
        removeValue = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return removeValue

    def insert(self, value):
        # insert the node to the end and then siftUp to rightful position
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
