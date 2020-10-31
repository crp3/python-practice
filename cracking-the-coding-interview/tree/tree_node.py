class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value < value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        elif self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.value, end=' ')

def create_default_tree():
    tree = Node(5)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(6)
    tree.insert(8)
    tree.insert(0)
    return tree