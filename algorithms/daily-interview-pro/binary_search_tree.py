class Node:
  def __init__(self, val, right=None, left=None):
    self.val = val
    self.right = right
    self.left = left

def create_default_bst():
  root = Node(8)
  root.left = Node(4)
  root.right = Node(12)

  root.left.left = Node(2)
  root.left.right = Node(6)

  root.right.left = Node(10)
  root.right.right = Node(14)
  return root

def level_order_traversal(root):
  layer = [root]
  while layer:
    new_layer = []

    print([node.val for node in layer])
    for node in layer:
      if node.left:
        new_layer.append(node.left)
      if node.right:
        new_layer.append(node.right)

    layer = new_layer
