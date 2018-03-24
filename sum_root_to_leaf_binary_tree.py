#!/usr/bin/env python3

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.data, self.data,
                                   self.right and self.right.data)


def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:  # Leaf.
        return partial_path_sum
    # Non-leaf.
    return (sum_root_to_leaf(tree.left, partial_path_sum) +
            sum_root_to_leaf(tree.right, partial_path_sum))


def main():
    #      1
    #    1   0
    #  0    1 0
    root = BinaryTreeNode(1)
    assert sum_root_to_leaf(root) == 1
    root.left = BinaryTreeNode(1)
    assert sum_root_to_leaf(root) == 3
    root.left.left = BinaryTreeNode(0)
    assert sum_root_to_leaf(root) == 6
    root.right = BinaryTreeNode(0)
    assert sum_root_to_leaf(root) == 8
    root.right.left = BinaryTreeNode(1)
    assert sum_root_to_leaf(root) == 11
    root.right.right = BinaryTreeNode(0)
    assert sum_root_to_leaf(root) == 15


if __name__ == '__main__':
    main()
