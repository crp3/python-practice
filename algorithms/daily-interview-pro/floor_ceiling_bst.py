from data_structures.binary_search_tree import *

def floor_ceiling_bst(root, target):
  current = root
  solution_stack = []

  while current:
    if current.val == target:
      return [current.val, current.val]

    if target > current.val:
      if current.right:
        if target < current.right.val:
          solution_stack.append([current.val, current.right.val])
          current = current.right
      else:
        if solution_stack == []:
          return [current.val, None]
        current = current.right
    else:
      if current.left:
        if target > current.left.val:
          solution_stack.append([current.left.val, current.val])
          current = current.left
      else:
        if solution_stack == []:
          return [None, current.val]
        current = current.left
  return solution_stack.pop()



if __name__ == '__main__':
  root = create_default_bst()
  level_order_traversal(root)
  assert floor_ceiling_bst(root, 5) == [4, 6]
