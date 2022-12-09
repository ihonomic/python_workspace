"""
- You will always need another variable to update a linkedList
tail = dummy. Where, tail is used to update dummy
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.head2 = None  # for two list questions ONLY

    def printList(self):
        head = self.head
        s = ""
        while head:
            s += str(head.data) + "-->"
            head = head.next
        print(s)

    def push(self, data):
        """Add from beginning"""
        node = Node(data, self.head)
        self.head = node
        return

    def append(self, data):
        """Add from end"""
        if self.head is None:
            self.head = Node(data, None)
            return

        head = self.head
        while head.next:
            head = head.next

        head.next = Node(data, None)

    def appendAll(self, data_list):
        head = self.head = None
        for data in data_list:
            self.append(data)

        ####    SECOND HEAD     ########################################

    def printList2(self):
        head2 = self.head2
        s = ""
        while head2:
            s += str(head2.data) + "-->"
            head2 = head2.next
        print(s, "<--- Second head")

    def appendList2(self, data):
        if self.head2 is None:
            self.head2 = Node(data, None)
            return

        head = self.head2
        while head.next:
            head = head.next
        head.next = Node(data, None)

    def appendAllToSecondHead(self, data_list):
        self.head2 = None
        for data in data_list:
            self.appendList2(data)

        ####   END SECOND HEAD     ####

    def getLength(self):
        head = self.head
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def sortList(self):
        """Sort list in ascending order (non-decending)
        - Merge sort
        Method : Recursively,
        1. get middle,
        2. sort left, sort right
        3. Merge left & right
        """

    def swapNodes(self, x, y):
        """Swap nodes without swapping data. Assume the list contains distinct, values, only do this
        if x and y exist and are different values
        Method 1  - Consider previous, If previous is none, i.e element is at beginning.
        """
        if x == y:  # 1.   Can't swap node of similar data
            return self.head

        #   Check if x, y exist
        prevX, currentX = None, self.head
        prevY, currentY = None, self.head

        while currentX and currentX.data != x:
            prevX = currentX
            currentX = currentX.next

        while currentY and currentY.data != y:
            prevY = currentY
            currentY = currentY.next

        # 2. Can't swap node, If x or y couldn't be found, i.e they loop to the end
        if currentX == None or currentY == None:
            return self.head

        # 3. If x was not at the start, link previous to currentY
        if prevX != None:
            prevX.next = currentY
        else:
            self.head = currentY

        # 4. If y was not at the start, link previous to currentX
        if prevY != None:
            prevY.next = currentX
        else:
            self.head = currentX

        # 5. Swap next pointers
        temp = currentX.next
        currentX.next = currentY.next
        currentY.next = temp

    def deleteNode(self, node):
        """
        - Given a node, that is not beginning or ending, remove the node from the list.
        [4,5,1,9], remove node 5 -> [4,1,9]
        [4,1,9], remove node 1 -> [4,5,9]

        Method 1 - Clone the given node with its next, (value & pointer) and then remove the next
        """
        node.val = node.next.val
        node.next = node.next.next

    def removeElements(self, target):
        """Remove all node that equals target.
        Slow & Fast pointers, Shift slow to fast if fast is not target.
        Take note if slow is still None, i.e the target is at the beginning..
        """
        slow, fast = None, self.head
        while fast:
            if fast.data == target:
                if (
                    slow is None
                ):  # if first element equals target, head is pointed to the next
                    head = fast.next
                else:
                    slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return self.head

    def removeDuplicates(self):
        """In a sorted list, Remove duplicate, All elements should be unique.
        Method 1 - Because the list is sorted,
                    comparing each node with the next, if similar, shift fast to next
        Method 2 - Use hashSet, hashMap to save previously seen, 0(n) space
        """
        fast = self.head

        while fast and fast.next:

            while (
                fast.next and fast.data == fast.next.data
            ):  # As long as it keeps re-occuring
                fast.next = fast.next.next

            fast = fast.next

    def removeDuplicatesUnsorted(self):
        """In an Unsorted list, Remove duplicate, All elements should be unique. Retain the order
        Method 1 - Use hashSet, hashMap to save previously seen, 0(n) space
        Method 2 - Sort the list 0(nlogn),
        """

    def removeAll_DuplicateSorted(self):
        """If element is duplicated, remove all of its kind
        [1,2,3,3,4,4,5] => [1,2,5]
        Method 1: HashMap - (time, space) complexity = 0(n), 0(n)
        Method 2: dummy head, ensure that the next value dummy would point to, has no
                similar value - use while looop to remove all
        """
        d = {}
        dummy = Node()
        tail = dummy

        fast = self.head

        while fast:
            if fast.val not in d:
                d[fast.val] = 1
            else:
                d[fast.val] += 1

            fast = fast.next

        for k, v in d.items():
            if v <= 1:
                tail.next = Node(k)
                tail = tail.next

        return dummy.next

    def removeNthNodeFromEnd(self, n):
        """
        - slow & fast pointers, fast-track 'fast' to nth position
        - move slow and new fast pointer until fast get to end, slow will be at the nth node from end.
        """
        dummy = Node()
        tail = dummy  # use to update dummy

        slow = fast = self.head

        for _ in range(1, n):
            fast = fast.next

        while fast and fast.next:
            tail.next = slow  # update tail pointers before slow shift to next
            tail = tail.next

            slow = slow.next
            fast = fast.next

        #   it stopped because fast has ended, so slow is at the nth node from end
        #   dummy can equal the next node after slow
        tail.next = slow.next

        return dummy.next

    def nthNodeFromEnd(self, n):
        """Find the nth Node from the end
        Method 1 - Move fast pointer to n position
        Method 2 - Substract total length from n and loop a single pointer to the position
        """
        slow = fast = self.head

        for _ in range(n):
            fast = fast.next

        #   Move pointer until fast becomes last
        while fast:
            slow = slow.next
            fast = fast.next

        #   slow should be at n from last
        print(slow.data)

    def findMiddleNode(self):
        """Find the middle element, of course if even, there are 2 middle elements,
        return second element.
         - Two pointers, Move slow pointer by 1 and fast pointer by 2 until fast gets to the end.
                   Slow will be at the middle.
                        - slow.next
                        - fast.next.next
        """
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)

    def countNodeOccurrence(self, data):
        """Count the number of times a given int appears
        Method 1 - Iterative (time, space) = 0(n), 0(1)
        Method 2 - Recursion  = 0(n), 0(n)
        """
        head = self.head
        count = 0

        #   ITERATIVE
        # while head:
        #     if head.data == data:
        #         count += 1
        #     head = head.next
        # print(count)

        # RECURSION
        def counter(head, key, count):
            if not head:
                print(count)
                return count

            if head.data == key:
                count += 1
                return counter(head.next, key, count)
            return counter(head.next, key, count)

        counter(head, data, count)

    def createLoop(self, n):
        """Create a loop by connecting the last node to the nth node"""
        loopNode = self.head
        for _ in range(1, n):
            loopNode = loopNode.next

        endNode = self.head
        while endNode.next:
            endNode = endNode.next

        endNode.next = loopNode
        print(f"last node {endNode.data} linked to ", loopNode.data)

    def detectLoop(self):
        """Find if the list has a loop.
        self.head.next.next.next = self.head.next

        Method 1 - Hash set => set(), return true, if current head already in set. (Leetcode 142-Medium)
        Method 2 - Flag each node, During the node instantiation, self.flag = 0,
        when traversing, update flag to 1.
        Method 3 - Floyd's Cycle- Finding algorithm (Using a fast & slow pointer), Fast move 2 steps,
        slow moves 1 step.
        If at any point, fast == slow, return true. But return false if fast approaches None
        Method 4 - Traverse & Change the node data, to anything (e.g -1),
        if -1 is found again, return True
        """
        # Initialize a loop linkedList
        self.createLoop(2)
        ...

    def detectAndCountNodesInLoop(self):
        """Find the length of nodes in a looped linkedList,
        i.e nodes that are contineously been traversedd
        Method 1 - Floyd's cycle. At the point where the fast and slow meet,
                   save it then traverse and count until you find the saved point, return the count
        """
        # Initialize a loop linkedList
        self.createLoop(2)

        slow = fast = self.head
        mutual_point = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                mutual_point = slow
                break

        numberOfNodes = 0
        head = mutual_point
        while head:
            numberOfNodes += 1
            head = head.next

            if head == mutual_point:
                print("Count of looping nodes =>", numberOfNodes)
                break

    def reverseLinkedList(self, listHead=None):
        """Reverse a LinkedList"""

        if not listHead:  # that means reverse everything
            listHead = self.head

        prev = None
        current = listHead
        next = None

        while current:  # Until prev becomes last head & current is shifted to None
            next = current.next
            current.next = prev
            prev = current
            current = next

        # self.head = prev  # set head to equal the reverse.
        # self.printList()

        return prev

    def reverseLinkedListRecursive(self):
        """Reverse a LinkedList Recursive approach"""

    def rotateRight(self, k):
        """Rotate List by k length
           [1,2,3,4,5], k = 2 => [4,5,1,2,3]
           [0,1,2], k = 4 => [2,0,1]
        - Limit k, k % len(arr) - incase k greater than the length
        - Loop to the kth node from the end,
           i.e Moving fast pointer ahead by k and then move both.
        - End the list
        - Link the second half nodes to the beginning
        """
        head_p = self.head
        len_head = self.get_length(head_p)

        if not len_head:
            return head

        k = k % len_head

        if not k:
            return head

        dummy = Node()
        tail = dummy

        slow = fast = head
        for _ in range(1, k):
            fast = fast.next

        while fast and fast.next:

            # update pointer
            tail.next = slow
            tail = tail.next

            slow = slow.next
            fast = fast.next

        #   End the list stored in dummy
        tail.next = None

        head = slow
        while head and head.next:
            head = head.next
        head.next = dummy.next

        return slow

    def isPalindrome(self):
        """
        Method 1 - Create an array stack, append from the linkedList and check if palindrome,
                    (time, space) = 0(n), 0(n)
        Method 2 - Reverse the linkedList - Second half
                    (time, space) = 0(n), 0(1)
        """
        slow = fast = self.head

        #   Find middle (slow)
        # Doing this, for even length, fast approaches None.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #   Reverse second half
        prev = self.reverseLinkedList(slow)

        #   check if palindrome
        left, right = self.head, prev

        while right:
            if left.data != right.data:
                print("Not Palindrome")
                return False
            left = left.next
            right = right.next
        print("Is palindrome")
        return True

    def reOrderList(self):
        """
        Re-order the list, such that the last element takes up even positions.
        [1,2,3,4] -> [1,4,2,3]
        [1,2,3,4,5] -> [1,5,2,4,3]
        Method 1 - Reverse second half
        """
        slow, fast = self.head, self.head.next  # fast is initally ahead

        #   find second half - by determining the middle, second half starts at slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        #   End the first half
        slow.next = None

        #   Reverse second half
        end = self.reverseLinkedList(second)

        print(second.data, end.data)

        #   Merge both halves
        first, second = self.head, end
        while second:  # Since second is more likely to be shorter
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first, second = temp1, temp2

    def pairSwap(self):
        """Swap 2 adjacent nodes consecutively.
        [1->2->3->4->5->6] => -[2>1->4->3->6->5]
        [1] => [1]
        [1->2->3->4->5] => [2->1->4->3->5]
        Method 1 - Swap data only
        """
        if self.head is None or self.head.next is None:
            return self.head
        fast = self.head

        while fast and fast.next:
            # swap
            fast.data, fast.next.data = fast.next.data, fast.data
            # # move pointer twice -
            fast = fast.next.next

    def moveLastToFirst(self):
        """Move Last to first
        [1->2->3->4->5] => [5->1->2->3->4]
        Method 1 - Get data of the last, point previous to last to None,
                push the data to first
        """
        if self.head is None or self.head.next is None:
            return self.head

        prev = fast = self.head
        while fast and fast.next:
            prev = fast
            fast = fast.next
        #   close previous
        prev.next = None

        # 1. push from beginning
        # self.push(fast.data)
        #                                    OR
        # 2. Re-point
        fast.next = self.head
        self.head = fast

    def merge2sortedLists(self, l1=None, l2=None):
        """
        - Merge 2 sorted lists
        [1,2,4,5] & [2,2,3] -> [1,2,2,2,3,4,5]
        """
        dummy = Node()
        left, right = l1 or self.head, l2 or self.head2
        tail = dummy  # to update dummy

        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

    def mergeKArrayOfList(self, lists=[]):
        """Given an array of linkedlists, Merge all in non-decending order
        [[1,2,3,4,5], [1,3,5,6], [0]] -> [0,1,1,2,3,3,4,5,5,6]
        NOTE:  I used the default head nodes to build the lists
        Method : Loop through the given lists by 2-steps, Take note for odd length (l2 = None)
                - Merge each lists per loop,
                - save the returns of the merge in an array
                - After every loop, reset the lists to the arrays of merge outcomes
            This happens until the lists size is less than 1.
        """
        lists = [self.head, self.head2]

        while len(lists) > 1:
            mergeLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > i + 1 else None  # for odd length

                #   merge both lists & save the return
                mergeLists.append(self.merge2sortedLists(l1, l2))

            lists = mergeLists

        return lists[0]

    def addTwoLinkedLists(self):
        """Add two linkedLists, Take notes of carryOver
        [2,4,3] + [5,6,4] = [7,0,8]
        [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
        NOTE: If one list runs out, default to 0
        """
        dummy = Node()
        tail = dummy  # Use to modify dummy
        l1, l2 = self.head, self.head2
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0

            total = val1 + val2 + carry
            carry, total = divmod(total, 10)

            #   Assign next pointer and move to next
            tail.next = Node(total)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Print dummy to see
        #         s = ''
        #         d = dummy.next
        #         while d:
        #             s += f"{str(d.data)}"
        #             d = d.next

        #         print(s)

        return dummy.next

    def intersectionOfTwoLists(self):
        """Both lists are sorted,  Return a new list of common elements
        A= [1,2,3,4,6] B= [2,4,6,8] -> [2,4,6]
        Method 1 - Using a dummy node. Add to dummy until A or B is None,
                -skip if elements are not similar, advance the list with smaller element
        """
        dummy = Node()
        tail = dummy  # pointer to alter node
        l1, l2 = self.head, self.head2

        while l1 and l2:
            if l1.data == l2.data:
                #   Add dummy pointer and update to next
                tail.next = l1
                tail = tail.next

                l1 = l1.next
                l2 = l2.next
            elif l1.data < l2.data:
                l1 = l1.next
            else:
                l2 = l2.next

        return dummy.next

    def getIntersectionPointOf2Lists(self):
        """Return the node where 2 lists first became similar.
        i.e one head got linked to another forming a 'Y' intersection
        Method 1 - Using two loops,
        Outer loop should compare its current value with each value of the next

        Question 2 - Leetcode 160.
        This question is more about checking for node that has the same ID, pointing to same location.
        Method - Loop to the end of both lists, if any becomes None, assign the pointer to the next list,
        This continues they intersect at the same node (Floyd)
        """

        headA, headB = self.head, self.head2

        while headA:
            while headB:
                if headA.data == headB.data:
                    print(headA.data)
                    return headA.data
                headB = headB.next
            headA = headA.next
        return None

        #       OR
        #       for every firstNode, go through all of second node
        firstNode = head1
        secondNode = head2

        while firstNode is not None:

            while secondNode is not None:
                if firstNode == secondNode:
                    return firstNode.data
                secondNode = secondNode.next
            secondNode = head2

            firstNode = firstNode.next

        return None

        # Question 2 - Leetcode 160
        one = headA
        two = headB
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one


if __name__ == "__main__":
    ll = LinkedList()
    # ll.push(6)

    ll.appendAll([1, 2, 3, 4, 5, 6])
    ll.appendAllToSecondHead([1, 3, 5, 6])

    ll.printList()
    # ll.printList2()
    # ll.nthNodeFromEnd(3)
    ll.findMiddleNode()
    # ll.countNodeOccurrence(3)
    # ll.detectAndCountNodesInLoop()
    # ll.isPalindrome()
    # ll.rotateRight(2)
    # ll.reverseLinkedList()
    # ll.reverseNodesKGroups(3)
    # ll.removeElements(6)

    # ll.reOrderList()      - Not understood
    # ll.removeDuplicates()
    # ll.swapNodes(3,4)

    # ll.pairSwap()
    # ll.moveLastToFirst()

    # ll.merge2sortedLists()
    # ll.mergeKArrayOfList()
    # ll.addTwoLinkedLists()

    # ll.intersectionOfTwoLists()
    # ll.getIntersectionPointOf2Lists()

    ll.printList()
