class Node:

    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        node = Node(data, itr, None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list: list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print('None')
            return

        itr = self.head
        s = ''
        while itr:
            s += f'{str(itr.data)} --> '

            itr = itr.next
        print(s)

    # ======================================
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        if self.head is None:
            print('None')
            return

        last_node = self.get_last_node()
        itr = last_node
        s = ''
        while itr:
            s += f'{itr.data} --> '
            itr = itr.prev

        print(s)

    # =============================================
    def get_length(self):
        count = 0
        if self.head is None:
            print(count)
            return

        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        print(count)

    def insert_at(self, index, data):
        if 0 > index >= self.get_length():
            raise Exception(f'{index} is not a valid index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if 0 > index >= self.get_length():
            raise Exception(f'{index} is not a valid index')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def deleteLinkedList(self):
        itr = self.head
        while itr:
            nextItr = itr.next

            del itr.data

            itr = nextItr


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_values(["A", "B", "C", "D"])
    # ll.print_forward()
    # ll.print_backward()
    ll.insert_at_beginning("Ihon")
    ll.deleteLinkedList()
    ll.get_length()
