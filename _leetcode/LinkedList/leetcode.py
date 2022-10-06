"""
707. Design Linked List
"""


class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        length = 0
        head = self.head

        while head:
            if index == length:
                return head.val
            length += 1
            head = head.next
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
            return

        self.head = Node(val, self.head)
        return self.head

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
            return

        head = self.head
        while head.next:                   # take note
            head = head.next

        head.next = Node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.getLength():
            self.addAtTail(val)
            return
        if index > self.getLength():
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # Stop before the index
                itr.next = Node(val, itr.next)
                break
            itr = itr.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 < index >= self.getLength():
            return

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # Stop before the index
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def getLength(self) -> int:
        head = self.head
        length = 0
        while head:
            length += 1
            head = head.next
        return length


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
