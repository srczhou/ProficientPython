#!/usr/bin/env python3
#from linked_list_prototype import ListNode
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next


def main():
    L = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

    temp = L
    while temp:
        print(temp.data, end = " ")
        temp = temp.next
    print()

    L = remove_kth_last(L, 3)
    assert L.data == 1 and L.next.data == 2 and L.next.next.data == 4 and L.next.next.next.data == 5

    temp = L
    while temp:
        print(temp.data, end = " ")
        temp = temp.next
    print()

if __name__ == '__main__':
    main()
