from data_structures.linked_list import *

def reverse(head):
  current = head
  prev = next_ = None

  while current:
    next_ = current.next
    current.next = prev
    prev = current
    current = next_

  return prev


if __name__ == '__main__':
  head = get_default_list()
  print_list(head)
  print_list(reverse(head))
