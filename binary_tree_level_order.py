#!/usr/bin/env python3
import collections

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.data, self.data,
                                   self.right and self.right.data)

def binary_tree_depth_order(tree):
    result, curr_depth_nodes = [], collections.deque([tree])
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                # Defer the null checks to the null test above.
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes = next_depth_nodes
    return result


def main():
    #      3
    #    2   5
    #  1    4 6
    # 10
    # 13
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(1)
    tree.left.left.left = BinaryTreeNode(10)
    tree.left.left.left.right = BinaryTreeNode(13)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    # should output 3
    #               2 5
    #               1 4 6
    #               10
    #               13
    assert binary_tree_depth_order(tree) == [[3], [2, 5], [1, 4, 6], [10], [13]]
    print(binary_tree_depth_order(tree))

if __name__ == '__main__':
    main()

