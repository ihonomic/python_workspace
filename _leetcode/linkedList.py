class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        # if not empty
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->  '
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next  # Keep iterating until you get to the end

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None  # clear existing
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if 0 < index >= self.get_length():
            raise Exception("Not a valid Index")

        if index == 0:
            self.head = self.head.next  # if required to remove the head
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(8)

    ll.insert_at_end(77)

    ll.insert_values(["mango", "banana", "grape", "oranges"])

    ll.print()

    ll.remove_at(2)

    ll.print()
    print('Length of my LinkedList: ', ll.get_length())
