""" Question 1 - Remove duplicates from linkedlist
    e.g: 1-1-3-4-4-4-5-6-6 --> 1-3-4-5-6
    Method: 0(n) time and 0(1) space
        -
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    dummy = LinkedList(None)
    tail = dummy
    curr = linkedList

    while curr:
        while curr.next and curr.value == curr.next.value:
            curr = curr.next
        tail.next = curr
        tail = curr
        curr = curr.next

    return dummy.next


""" Question 2 - LinkedList construction. Doubly LinkedList
        - Add at the beginning. setHead(node)
        - Add at the tail. setTail(node)
        - Insert before a node, insertBefore(node, nodeToInsert), 
            . Remove all occurrences of "nodeToInsert" and insert it before "node"
        - Insert after a node , insertAfter(node, nodeToInsert),
            . Remove all occurrences of "nodeToInsert" and insert it after "node"
        - Insert a node at an index location, insertAtPosition(position, nodeToInsert). Note: Index count starts at 1
        - Remove all nodes with values, removeNodesWithValue(value)
        - Remove a node, remove(node)
        - Check if node with value exist in the list, containsNodeWithValue(value), return True/False
        
        e.g: 1 <-> 2 <-> 3<-> 4<->5
        setHead(4): 4<->1<->2<->3<->5
        setTail(6):  4<->1<->2<->3<->5 <->6
        insertBefore(6,3): 4<->1<->2<->5 <->3<->6
        insertAfter(6,3): 4<->1<->2<->5 <->3<->6<->3
        insertAtPosition(1,3): 3<->4<->1<->2<->5 <->3<->6<->3
        removeNodesWithValue(3): 4<->1<->2<->5<->6
        remove(2): 4<->1<->5<->6
        containsNodeWithValue(5): True
            
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 0(1) time | 0(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # 0(1) time | 0(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # 0(1) time | 0(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
            # Wherever nodeToInsert is, on the list, move it before node
        # search for it and remove it first and insert it before the node
        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # 0(1) time | 0(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
            # Wherever nodeToInsert is, on the list, move it after node
        # search for it and remove it first and insert it after the node
        self.remove(nodeToInsert)

        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        # Update the node pointer
        node.next = nodeToInsert

    # 0(p) time | 0(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        current = 1
        while node is not None and current != position:
            node = node.next
            current += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # 0(n) time | 0(1) space
    def removeNodesWithValue(self, value):
        # Remove all cases of value
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # 0(1) time | 0(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        # destroy the node pointers
        node.next = None
        node.prev = None

    # 0(n) time | 0(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node and node.value == value:
                return True
            node = node.next
        return False


""" Question 3 - Remove kth node from the end 
    Write a func that takes in a singly linkedlist and k value. Remove the kth node from the end.
    Removal should be done in-place
    e.g: 1-1-3-4-4-4-5-6-6, k = 2 --> 1-1-3-4-4-4-5-6
    Method: 0(n) time and 0(1) space
        - Take note of K wrapping about.
        - If k is at index 0, i.e the  node to remove is the first, drag every node backwards
"""


def removeKthNodeFromEnd(head, k):
    slow = head
    fast = head
    k = k % getLinkedListLength(head)
    # if k is at index 0, i.e the  node to remove is the first,
    # drag every node backwards
    if not k:
        head.value = head.next.value
        head.next = head.next.next
        return

    for _ in range(k):
        fast = fast.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next


def getLinkedListLength(head):
    headPointer = head
    length = 0
    while headPointer:
        length += 1
        headPointer = headPointer.next
    return length


""" Question 4 - Sum of Linked Lists
    Write a func that takes in a 2 singly linkedlist and return a new linkedlist where its nodes are sums of 
    both linkedlists
    e.g: l1 = 2->4->7->1,    l2 = 9->4->5    -->    2->2->9->1
    Method: 0(max(n1, n2)) time | 0(max(n1, n2)) space
        - Use a dummy node to collect the sum
        - consider carry
"""


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    dummyList = LinkedList(0)
    dummyTail = dummyList

    carry = 0
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        runningSum = 0
        runningSum += nodeOne.value if nodeOne else 0
        runningSum += nodeTwo.value if nodeTwo else 0
        runningSum += carry if carry else 0

        # update both list pointers
        nodeOne = nodeOne.next if nodeOne else None
        nodeTwo = nodeTwo.next if nodeTwo else None

        # if previous carray has been added, we need to reset
        # TAKE NOTE
        carry, digit = divmod(runningSum, 10)

        dummyTail.next = LinkedList(digit)
        dummyTail = dummyTail.next

    return dummyList.next


""" Question 5 - Find loop
    In a linkedlist that has a loop, Write a func that returns the node where a linkedlist loops starts 
    e.g: 0 -> 1 -> 2-> 3-> 4-> 5
                        |              |
                        8 <-- 7 <--  6    // loop starts at node 2
    Method: 0(n) time | 0(1) space
        The idea behind finding the node where the loop of a linkedList starts.
        (FLOYD's Algorithm)
        Use a slow pointer and a fast pointer moving one and twice respectively. If at 
        any point the slow equals fast, A LOOP IS DETECTED. 
    
        Now to find the start of the loop, move a third pointer from the beginning and
        move the slow pointer about its trapped loop, at the point where the 
        slow and third pointer meets is the start of the loop
"""


def findLoop(head):
    slow = head.next
    fast = head.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    third = head
    while third != slow:
        third = third.next
        slow = slow.next
    return third


""" Question 6 - Reverse Linked Lists
    Write a func that takes a linkedlist and reverses it 
    e.g: 0 -> 1 -> 2-> 3-> 4-> 5        -->       5->4->3->2->1->0     
    Method: 0(n) time | 0(1) space
        Next node points to previous
        previous becomes current
"""


def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next = current.next

        current.next = prev
        prev = current

        current = next

    return prev


""" Question 7 - Merge linked lists
    Write a func that takes a 2 sorted linkedlist and merges it
    e.g: l1 =  2 -> 6 -> 7-> 8 , l2 = 1->3->4->5->9->10
      -->   1 ->  2 ->  3 -> 4 -> 5-> 6-> 7-> 8-> 9-> 10
    Method: 0(n +m) time | 0(1) space
        Use a dummy head, while both lists haven't exhuated, add the smallest node between both lists
         to dummy. The loops ends when one is exhuasted. Handle it by pointing the dummy to whatever is left
"""


def mergeLinkedLists(headOne, headTwo):
    dummy = LinkedList(0)
    tail = dummy

    listOne = headOne
    listTwo = headTwo

    while listOne is not None and listTwo is not None:
        if listOne.value <= listTwo.value:
            # Update pointer
            tail.next = listOne
            listOne = listOne.next
        else:
            # Update pointer
            tail.next = listTwo
            listTwo = listTwo.next
        tail = tail.next

    if listOne:
        tail.next = listOne
    if listTwo:
        tail.next = listTwo

    return dummy.next


""" Question 8 - Shift Linked List
    Write a func that takes a head of a linkedLists and an integer k, shift the lists in place by k positions.
    That is, Wrap it around and then return the new head.
     k can also be negative and can also wrap around (Rotate List by k length)
    e.g:[1,2,3,4,5], k = 2 => [4,5,1,2,3]
        [0,1,2], k = 4 => [2,0,1].
    Method: 0(n +m) time | 0(1) space
     - Get the length and the last node.
     - Loop to the offset where it's after nodes are expected to move to the beginning
"""


def shiftLinkedList(head, k):

    listLength, lastNode = getListLengthAndLastNode(head)

    k = k % listLength  # handle wrapping
    offset = abs(k) % listLength  # handle negative

    if k == 0 or offset == 0:  # Don't do anything if no index to wrap about
        return head

    newTailPosition = listLength - offset if k > 0 else offset
    # Go to the new expected tail, the next node is the new head
    # so end the tail and begin new head
    newTail = head
    for _ in range(1, newTailPosition):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None

    lastNode.next = head
    return newHead


def getListLengthAndLastNode(head):
    length = 1
    node = head
    while node.next is not None:
        length += 1
        node = node.next
    return length, node


""" Question 9 - LRU Cache
    Implement a LRUcache class for a Least recently used cache that does the following in constant time:
        - Insert key-value pair, insertKeyValuePair()
        - Retrieveing key-value pair, getValueFromKey()
        - Retrieveing the most recently used (the most recently inserted or retrieved) key, getMostRecentKey()
    The class should store a maxSize at initialization, which represent the maximum number of key-value pair the 
    cache can store. If a new key-value pair is inserted, and the storage has reached its maxSize, 
    the least recently used cache should be evicted.
    e.g: LRUCache(3) // Instatialize as the maxSize
        insertKeyValuePair("b", 2)
        insertKeyValuePair("a", 1)
        insertKeyValuePair("c", 3)
        getMostRecentKey() --> ''c''
        getValueFromKey("a") --> 1
        getMostRecentKey() --> ''a' // because a was recently used (retrieved)
        insertKeyValuePair("d", 4) 
        getValueFromKey("b") --> None // because hasn't been used recently and was evicted 
        insertKeyValuePair("a", 5) // a has been replaced 
        getValueFromKey("a") --> 5
    Method: 
    - The idea behind LRU cache is that when the maxsize is exhuausted, the saved up item that were 
    not modified or requested is removed. (Just like the name suggest)
    - Use a double linkedlist and a dict, whatever value that was recently requested or inserted, set it as the head
    - If a new pair is entered and the maxSize has reached, remove the tail
"""


""" Question 10 - Rearrange Linked List
    Write a func that takes in the head of a linkedlists and an interger k, rearrange the list in-place
    and return its new head. The arrangement should be in a way that node less than k should appear before it
    and those higher than k should appear after it. THE ORDER SHOULD BE RETAINED 
    e.g: lists = [3,0,5,2,1,4] , k = 3 --> [0,2,1,3,5,4]
    Method: 0(n) time | 0(1) space
     - Create 3 dummy nodes, for values smaller, equal and greater
    - Connect dummy nodes middle to large, connect smaller to middle and remember to close large
"""


def rearrangeLinkedList(head, k):
    smallPointer = dummySmallThanK = LinkedList(0)
    equalPointer = dummyEqualThanK = LinkedList(0)
    largePointer = dummyLargeThanK = LinkedList(0)

    node = head
    while node is not None:
        if node.value < k:
            smallPointer.next = node
            smallPointer = smallPointer.next
        elif node.value == k:
            equalPointer.next = node
            equalPointer = equalPointer.next
        else:
            largePointer.next = node
            largePointer = largePointer.next

        node = node.next

    # Sequentially connect equals to larges and then connect
    # smaller to equals. Oh, also end large
    equalPointer.next = dummyLargeThanK.next
    smallPointer.next = dummyEqualThanK.next
    largePointer.next = None

    return dummySmallThanK.next


""" Question 11 - LinkedList palindrome
    Write a func that return True or false if linkedlist is a palindrome.
    e.g: [0,1,2,2,1,0] --> True
    Method: 0(n) time | 0(1)
        Reverse the second half of the list. Find the middle 
        Compare the first half and the second half 
"""


def linkedListPalindrome(head):
    firstHalf = head
    middle = getMiddleHead(head)
    secondHalf = reverseSecondHalf(middle)

    while firstHalf and secondHalf:
        if firstHalf.value != secondHalf.value:
            return False
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next
    return True


def getMiddleHead(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverseSecondHalf(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


""" Question 12 - Zip linkedList
    Write a func that zips the linkedList in place. A zip linkedlist is in the following order:
    1st node -> last node -> 2nd node -> last-1 node -> 3rd node -> last-2 node 
    e.g: [1,2,3,4,5,6] --> [1,6,2,5,3,4]
    Method: 0(n) time | 0(1) space
         - You can't zip a lists less than 4 nodes. 
        - Split the lists into 2 halves 
        - reverse the second half and merge both, consider first half and then second half until both exhusted
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):

    if linkedList.next is None or linkedList.next.next is None:
        return linkedList

    firstHalf = linkedList
    lastHalf = splitLinkedList(linkedList)
    secondHalf = reverseLinkedList(lastHalf)

    # start merging
    dummyList = LinkedList(0)
    dummyTail = dummyList

    while firstHalf is not None and secondHalf is not None:
        if firstHalf:
            dummyTail.next = firstHalf
            firstHalf = firstHalf.next
            dummyTail = dummyTail.next

        if secondHalf:
            dummyTail.next = secondHalf
            secondHalf = secondHalf.next
            dummyTail = dummyTail.next

    dummyTail.next = None
    return dummyList.next


def splitLinkedList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


""" Question 13 - Node Swap
    Write a func that takes in the head of a singly linkedlist and swap every pair of adjacent nodes (in-place)
    return its new head
    e.g: head = [0,1,2,3,4,5] --> [1,0,3,2,5,4]
    Method 1: 0(n) time | 0(1) space
        Swap only the value
    Method 2:
        Swap the nodes
"""


def nodeSwap(head):
    # 0(n) time | 0(1) space
    fast = head
    while fast and fast.next:
        fast.value, fast.next.value = fast.next.value, fast.value
        fast = fast.next.next
    return head
