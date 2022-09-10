class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data, None, current)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        if self.head is None:
            return 0

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        return count

    def search(self, key):
        if self.head is None:
            print('False')
            return False

        current = self.head
        while current:
            if current.data == key:
                print("True")
                return True
            current = current.next

        print('False')
        return False

    def returnNodeAtIndex(self, index):
        ''' Return the data found at the given index '''
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return

        if index == 0:
            print(self.head.data)
            return self.head.data

        current = self.head
        count = 0
        while current:
            if count == index:
                print(current.data)
                return current.data

            current = current.next
            count += 1

        return current.data

    def returnReverseNodeAtIndex(self, index):
        ''' Return node of index from the end '''
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return

        #   Method 1 - Count the nodes, sunstract from the index
        current = self.head
        for _ in range(0, self.get_length() - index):
            current = current.next

        print(current.data)


def searchLinkedList():
    arr = [14, 21, 11, 30, 10]
    key = 14

    #   insert
    ll = LinkedList()
    ll.insert_values(arr)
    # ll.search(key)
    # ll.get_length()
    # ll.returnNodeAtIndex(1)
    ll.returnReverseNodeAtIndex(0)


searchLinkedList()
