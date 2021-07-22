from linkedlist import *

def kth_to_n(head, k):
    current = head
    n = 0

    while current:
        n += 1
        current = current.next
    
    val = n - k - 1

    current = head
    for i in range(val):
        current = current.next

    return current.val



if __name__ == '__main__':
   l1 = get_default_list()
   print_list(l1)
   print(kth_to_n(l1, 2))
   