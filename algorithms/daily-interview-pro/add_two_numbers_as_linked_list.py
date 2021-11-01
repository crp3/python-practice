from linkedlist import *

def add_two_numbers(l1, l2):
  c1, c2 = l1, l2
  carry_out = 0
  head = ListNode(0)
  c3 = head

  while c1 and c2:
    sum_ = c1.val + c2.val + carry_out
    carry_out = sum_ // 10
    mod_sum = sum_ % 10
    c3.next = ListNode(mod_sum)
    c3 = c3.next
    c1 = c1.next
    c2 = c2.next

  while c1:
    sum_ = c1.val + carry_out
    carry_out = sum_ // 10
    mod_sum = sum_ % 10
    c3.next = ListNode(mod_sum)
    c3 = c3.next
    c1 = c1.next
  
  while c2:
    sum_ = c2.val + carry_out
    carry_out = sum_ // 10
    mod_sum = sum_ % 10
    c3.next = ListNode(mod_sum)
    c3 = c3.next
    c2 = c2.next

  if carry_out != 0:
    c3.next = ListNode(carry_out)

  return head.next

if __name__ == '__main__':
  l1 = get_default_list()
  l2 = get_default_list()
  print_list(l1)
  print_list(add_two_numbers(l1, l2))
