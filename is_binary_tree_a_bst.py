#!/usr/bin/env python3
import random
import sys
import collections
#from binary_tree_utils import generate_rand_binary_tree

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.data, self.data,
                                   self.right and self.right.data)

## O(n)
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and
            is_binary_tree_bst(tree.right, tree.data, high_range))


def is_binary_tree_bst_alternative(tree):
    def inorder_traversal(tree):
        if not tree:
            return True
        elif not inorder_traversal(tree.left):
            return False
        elif prev[0] and prev[0].data > tree.data:
            return False
        prev[0] = tree
        return inorder_traversal(tree.right)
    prev = [None]
    return inorder_traversal(tree)

# BFS manner, O(n)
def is_binary_tree_bst2(tree):
    QueueEntry = collections.namedtuple('QueueEntry',
                                        ('node', 'lower', 'upper'))
    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]
    return True

def test():
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    # should output True.
    assert is_binary_tree_bst(tree)
    assert is_binary_tree_bst_alternative(tree)
    #      10
    #    2   5
    #  1    4 6
    tree.data = 10
    # should output False.
    assert not is_binary_tree_bst(tree)
    assert not is_binary_tree_bst_alternative(tree)
    # should output True.
    assert is_binary_tree_bst(None)
    assert is_binary_tree_bst_alternative(None)

    ##### Same test for is_binary_tree_bst2
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    # should output True.
    assert is_binary_tree_bst2(tree)
    assert is_binary_tree_bst_alternative(tree)
    #      10
    #    2   5
    #  1    4 6
    tree.data = 10
    # should output False.
    assert not is_binary_tree_bst2(tree)
    assert not is_binary_tree_bst_alternative(tree)
    # should output True.
    assert is_binary_tree_bst2(None)
    assert is_binary_tree_bst_alternative(None)

if __name__ == '__main__':
    test()
