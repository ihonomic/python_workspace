class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        head = self.head
        s = ""
        while head:
            s += str(head.data)+'-->'
            head = head.next
        print(s)

    def push(self, data):
        """ Add from beginning """
        node = Node(data, self.head)
        self.head = node
        return

    def append(self, data):
        """ Add from end """
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

    def getLength(self):
        head = self.head
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def swapNodes(self, x, y):
        """ Swap nodes without swapping data. Assume the list contains distinct, values, only do this 
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

    def removeElements(self, target):
        """ Remove all node that equals target. 
        Slow & Fast pointers, Shift slow to fast if fast is not target.
        Take note if slow is still None, i.e the target is at the beginning.. 
        """
        slow, fast = None, self.head
        while fast:
            if fast.data == target:
                if slow is None:    # if first element equals target, head is pointed to the next
                    head = fast.next
                else:
                    slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return self.head

    def removeDuplicates(self):
        """ In a sorted list, Remove duplicate, All elements should be unique. 
        Method 1 - Because the list is sorted,
                    comparing each node with the next, if similar, shift fast to next
        Method 2 - Use hashSet, hashMap to save previously seen, 0(n) space
        """
        fast = self.head

        while fast and fast.next:
            if fast.data == fast.next.data:
                fast.next = fast.next.next
            else:
                fast = fast.next

    def removeDuplicatesUnsorted(self):
        """ In an Unsorted list, Remove duplicate, All elements should be unique. Retain the order 
        Method 1 - Use hashSet, hashMap to save previously seen, 0(n) space
        Method 2 - Sort the list 0(nlogn), 
        """

    def nthNodeFromEnd(self, n):
        """ Find the nth Node from the end
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
        """ Find the middle element, of course if even, there are 2 middle elements, 
            return second element.
             - Two pointers, Move slow pointer by 1 and fast pointer by 2 until fast gets to the end. 
                       Slow will be at the middle. 
                            - slow.next
                            - fast.next.next
        """
        slow = fast = self.head
        while fast:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)

    def countNodeOccurrence(self, data):
        """ Count the number of times a given int appears
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
        """ Create a loop by connecting the last node to the nth node """
        loopNode = self.head
        for _ in range(1, n):
            loopNode = loopNode.next

        endNode = self.head
        while endNode.next:
            endNode = endNode.next

        endNode.next = loopNode
        print(f"last node {endNode.data} linked to ", loopNode.data)

    def detectLoop(self):
        """ Find if the list has a loop. 
        self.head.next.next.next = self.head.next

        Method 1 - Hash set => set(), return true, if current head already in set. (Leetcode 142-Medium)
        Method 2 - Flag each node, During the node instantiation, self.flag = 0, 
        when traversing, update flag to 1.
        Method 3 - Floyd's Cycle- Finding algorithm (Using a fast & slow pointer), Fast move 2 steps, 
        slow moves 1 step. If at any point, fast == slow, return true. But return false if fast approaches None
        Method 4 - Traverse & Change the node data, to anything (e.g -1), if -1 is found again, return True
        """
        # Initialize a loop linkedList
        self.createLoop(2)
        ...

    def detectAndCountNodesInLoop(self):
        """ Find the length of nodes in a looped linkedList, 
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
        """ Reverse a LinkedList """

        if not listHead:    # that means reverse everything
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
        """ Reverse a LinkedList Recursive approach """

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

    def reOrderEvenOdd(self):
        """ While retaining the order, take all even to one-side.
        Method 1 - Easily done with linear space -> append to array and build new linkedList
        Method 2 -  
        """
        stack = []
        while self.head:
            stack.append(self.head.data)
            self.head = self.head.next

        # Sort
        i = 0
        for j in range(len(stack)):
            if stack[j] % 2 == 0:
                stack[i], stack[j] = stack[j], stack[i]
                i += 1

        #   build linkedlist
        for i in range(len(stack)):
            self.append(stack[i])

        """Method 2 """

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


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(6)
    ll.appendAll([1, 2, 3, 4, 5])
    ll.printList()
    # ll.nthNodeFromEnd(3)
    # ll.findMiddleNode()
    # ll.countNodeOccurrence(3)
    # ll.detectAndCountNodesInLoop()
    # ll.isPalindrome()
    # ll.reverseLinkedList()
    # ll.removeElements(6)

    # ll.reOrderList()      - Not understood
    # ll.removeDuplicates()
    # ll.swapNodes(3,4)
    ll.reOrderEvenOdd()

    ll.printList()
