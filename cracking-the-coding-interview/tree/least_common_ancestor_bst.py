from tree_node import create_default_bst

def least_common_ancestor(root, value_one, value_two):
    path_one = path(root, value_one)
    path_two = path(root, value_two)
    index = 0

    while index < len(path_one) and index < len(path_two):
        if path_one[index] != path_two[index]:
            break
        result = path_one[index]
        index += 1

    return result
    

def path(root, value):

    ''' this function assumes the value is always present inside the tree '''

    path = []
    node = root

    while node.value != value:
        path.append(node.value)
        if value > node.value:
            node = node.right
        else:
            node = node.left
    
    path.append(value)

    return path

if __name__ == '__main__':
    tree = create_default_bst()
    assert least_common_ancestor(tree, 0, 5) == 5
    assert least_common_ancestor(tree, 0, 4) == 3
    assert least_common_ancestor(tree, 8, 6) == 7
    assert least_common_ancestor(tree, 2, 8) == 5