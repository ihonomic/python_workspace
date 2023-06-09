import heapq

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
        # Heapify - start building heap from the middle
        # get the first parentIdx by obtaining the last parent, and then reverse it

        # [3,7,|1|,2,5,6,8] --> [3,1,|7|,2,5,6,8] --> [1,3,|7|,2,5,6,8]
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
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
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removeValue

    def insert(self, value):
        # insert the node to the end and then siftUp to rightful position
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


""" Question 2 - Contineous Media
    Define a class with contineous insertion of a number, using insert method 
    Retrieve the median in 0(1) time, using getMedian method 
    e.g: ContinuousMedianHandler() // 
            insert(5): -
            insert(10) - 
            getMedian() - 7.5
            insert(100) - 
            getMedian() - 10
    Method : 0(nlogn) time | 0(n) space
"""


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.array = []

    # 0(nlogn) time | 0(n) space
    def insert(self, number):
        self.array.append(number)
        self.array.sort()
        middleIdx = (len(self.array) - 1) // 2
        # if odd length
        if len(self.array) % 2:
            self.median = self.array[middleIdx]
        else:
            self.median = (self.array[middleIdx] + self.array[middleIdx + 1]) / 2

    def getMedian(self):
        return self.median


""" Question 3 - Sort K-sorted array 
     Given an array and a value k , return the sorted version of the array. Either sort the array in place or 
     return a new array. 
     NOTE: k indicates that each elements are at most k positions from their sorted position
    e.g: array=[3, 2, 1, 5, 4, 7, 6, 5] k=3 --> [1, 2, 3, 4, 5, 5, 6, 7]
    Method 1: 0(nlogn) time | 0(n) space
        Use heap sort, No need to consider k 
    Method 2: 0(nlogk) time | 0(k) space
          Since we're sure the elements are just k-range away from their original position. 
        We need to consider sorting the array by spliting it into k-first-half.
        As soon as we pop off the minimum value from the heap part, we push-in another value
        from the unsorted part. 
"""


def sortKSortedArray(array, k):
    # 0(nlogk) time | 0(k) space

    # array=[3,2,1,5, | 4,7,6,5] k=3
    #        1,         |
    heap = array[0:k + 1]
    heapq.heapify(heap)
    sortedIdx = 0
    for idx in range(k + 1, len(array)):
        array[sortedIdx] = heapq.heappop(heap)  # pop off the minimum
        sortedIdx += 1
        heapq.heappush(heap, array[idx])  # add another value from the unsorted part

    # If there are any value left in the heap?
    while len(heap) > 0:
        array[sortedIdx] = heapq.heappop(heap)
        sortedIdx += 1
    return array


""" Question 4 - Laptop Rentals 
     Given an array representing the time intervals each students in a class want to use a laptop. 
     You're charged with supplying laptops for each students. 
     If a student has finished using his allocated laptop, the laptop can be given to another student who is 
     about to commence use but a laptop still under used by a student can not be given to another student whose
     time is to use a laptop. 
     Return the number of laptops that can be used by all students 
    e.g: times=[
        [0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]
    ]   -->   3
    Method 1:   0(nlogn) time | 0(n) space
        Sort each time interval by their starting time. 
        Use a min-heap to store overlaps times (endTimes)
            i.e if the previous endTime is more than the incoming starttime, It is considered overlapping
            This also means that a new laptop has to be allocated. 
            but if at anytime the saved up endtimes no-longer overlaps the incoming interval, a previous laptop 
            has to be given to the incoming student
        return the total allocated laptop
    Method 2: 0(n) time | 0(1) space
"""''


def laptopRentals(times):
    # 0(nlogn) time | 0(n) space

    times.sort(key=lambda item: item[0])
    allocatedLaptops = []
    heapq.heapify(allocatedLaptops)
    for currStart, currEnd in times:
        # if the first laptop used by a student has ended, another student can use the laptop
        if allocatedLaptops and allocatedLaptops[0] <= currStart:
            heapq.heapreplace(allocatedLaptops, currEnd)
        else:
            heapq.heappush(allocatedLaptops, currEnd)

    # count how many laptops was used
    return len(allocatedLaptops)


"""  Question 5 - Merge sorted array
    Given an array of subarrays, merge the arrays and sort it 
    e.g : arrays=[
        [1, 5, 9, 21], 
        [-1, 0], 
        [-124, 81, 121],
        [3, 6, 12, 20, 150]
    ] --> [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
    Method : 0(k + nlogn ) time | 0(k + n) space

"""


def mergeSortedArrays(arrays):
    # 0(k) time | 0(k) space
    mergedArrays = []
    for subarray in arrays:
        mergedArrays += subarray

    # 0(nlogn) time | 0(n) space -- Sort this using any sorting techniques. e.g heap sort
    mergedArrays.sort()

    return mergedArrays
