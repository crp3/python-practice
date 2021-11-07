from data_structures.binary_search_tree import *

def invert_binary_tree(root):
    if root:
        root.left, root.right = root.right, root.left
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)

if __name__ == '__main__':
    root = create_default_bst()
    invert_binary_tree(root)
    level_order_traversal(root)