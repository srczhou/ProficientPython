#!/usr/bin/env python3

#from linked_list_prototype import ListNode
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


# O(n) time, O(1) space
def overlapping_no_cycle_lists(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1  # L2 is the longer list
    # Advances the longer list to get equal length lists.
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next

    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1  # None implies there is no overlap between L1 and L2.


def main():
    # L1: 1->2->3->None
    L1 = ListNode(1, ListNode(2, ListNode(3, None)))
    L2 = L1.next.next
    assert overlapping_no_cycle_lists(L1, L2).data == 3
    # L2: 4->5->None
    L2 = ListNode(4, ListNode(5, None))
    assert not overlapping_no_cycle_lists(L1, L2)


if __name__ == '__main__':
    main()
