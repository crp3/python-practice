from linkedlist import *

def remove_duplicates(head):
    current = head
    seen = set([current.val])

    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next
    
    return head


if __name__ == '__main__':
   l1 = get_default_list()
   print_list(l1)
   remove_duplicates(l1)
   print_list(l1)
   
   l1 = get_six_and_one()
   print_list(l1)
   remove_duplicates(l1)
   print_list(l1)