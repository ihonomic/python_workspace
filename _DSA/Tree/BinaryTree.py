
class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Don't add duplicate
        if data == self.data:
            return

        if data < self.data:
            #   add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            #   add in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #   visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #   visit root
        elements.append(self.data)

        #   visit right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            #   value might be in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False  # Value doesn't exist

        if val > self.data:
            #   value might be in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)  # after deleting assign new
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val  # copy the minimum to replace that to be deleted
            self.right = self.right.delete(min_val)

        return self

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


#   Helper method to build tree


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(21))
    numbers_tree.delete(17)
    print(numbers_tree.in_order_traversal())
