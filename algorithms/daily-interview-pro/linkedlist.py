class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(head):
    current = head
    
    while current:
        print(f' {current.val} ->', end='')
        current = current.next
    print(' None')

def get_default_list():
    l1 = ListNode(3)
    l2 = ListNode(1)
    l3 = ListNode(4)
    l4 = ListNode(2)
    l5 = ListNode(5)
    l6 = ListNode(1)
    l7 = ListNode(6)
    l6.next = l7
    l5.next = l6
    l4.next = l5
    l3.next = l4
    l2.next = l3
    l1.next = l2
    return l1

def get_six_and_one():
    l1 = ListNode(6)
    l2 = ListNode(1)
    l3 = ListNode(1)
    l4 = ListNode(6)
    l5 = ListNode(1)
    l6 = ListNode(1)
    l7 = ListNode(6)
    l6.next = l7
    l5.next = l6
    l4.next = l5
    l3.next = l4
    l2.next = l3
    l1.next = l2
    return l1
