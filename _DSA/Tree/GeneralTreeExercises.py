class Node:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """ count the node ancestors """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, display_type):

        spaces = ' ' * self.get_level() * 3

        if display_type == 'both':
            print(f'{spaces}|__ {self.name} ({self.designation})')
        elif display_type == 'name':
            print(f'{spaces}|__ {self.name}')
        else:
            print(f'{spaces}|__ {self.designation}')

        if self.children:
            for child in self.children:  # Recursion
                child.print_tree(display_type)


def build_management_tree():
    root = Node("Ihonosetale", "CEO")
    # `1.`
    cto = Node("Chinmay", "CTO")

    infra_head = Node("Vishwa", "Infrastructure Head")
    infra_head.add_child(Node("Dhaval", "Cloud manager"))
    infra_head.add_child(Node("Abhijit", "App manager"))

    cto.add_child(infra_head)

    cto.add_child(Node("Aamir", "Application Head"))

    #   2.
    hr = Node("Gel", "HR Head")
    hr.add_child(Node("Peter", "Recruitment manager"))
    hr.add_child(Node("Wagas", "Policy manager"))

    root.add_child(cto)
    root.add_child(hr)

    return root


if __name__ == '__main__':
    root = build_management_tree()
    # root.print_tree("name")
    # root.print_tree("designation")
    root.print_tree("both")
