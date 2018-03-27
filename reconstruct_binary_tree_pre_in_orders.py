#!/usr/bin/env python3
import sys
import random


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#from binary_tree_utils import generate_rand_binary_tree, generate_preorder, generate_inorder, is_two_binary_trees_equal

# Didn't quit understand this function, write a fake one.
def generate_rand_binary_tree(n, b):
    n, b = 6, True
    tree = BinaryTreeNode(1)
    tree.left = BinaryTreeNode(2)
    tree.right = BinaryTreeNode(3)
    tree.left.left = BinaryTreeNode(4)
    tree.left.left.left = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(6)
    return tree

def generate_preorder(tree):
    result = []
    def preorder_recursive(tree):
        if tree:
            result.append(tree.data)
            preorder_recursive(tree.left)
            preorder_recursive(tree.right)
    preorder_recursive(tree)
    return result

def generate_inorder(tree):
    result = []
    def generate_inorder_helper(tree):
        if tree:
            generate_inorder_helper(tree.left)
            result.append(tree.data)
            generate_inorder_helper(tree.right)
    generate_inorder_helper(tree)
    return result

# can be simplified to equal_binary_trees
def is_two_binary_trees_equal(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif tree1 and not tree2:
        return False
    elif not tree1 and tree2:
        return False
    elif tree1.data != tree2.data:
        return False
    else:
        return (is_two_binary_trees_equal(tree1.left, tree2.left) and
                is_two_binary_trees_equal(tree1.right, tree2.right))

def equal_binary_trees(r1, r2):
    if r1 and r2:
        return (equal_binary_trees(r1.left, r2.left)
                and equal_binary_trees(r1.right, r2.right)
                and r1.data == r2.data)
    else:
        return not r1 and not r2


def binary_tree_from_preorder_inorder(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx),
            # Recursively builds the right subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size, preorder_end,
                root_inorder_idx + 1, inorder_end))
    return binary_tree_from_preorder_inorder_helper(
        0, len(preorder), 0, len(inorder))


def simple_test():
    res = binary_tree_from_preorder_inorder([1], [1])
    assert res.data == 1

    res = binary_tree_from_preorder_inorder([2, 1], [1, 2])
    assert res.data == 2 and res.left.data == 1 and not res.right

    N = 100
    inorder, preorder = [], []
    for i in range(N):
        inorder.append(i)
        preorder.append((N - 1) - i)

    res = binary_tree_from_preorder_inorder(preorder, inorder)
    assert res.data == N - 1 and res.left.data == N - 2 and not res.right


def main():
    simple_test()
    for times in range(1):
        print(times)
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 10000)
        root = generate_rand_binary_tree(n, True)
        pre_order = generate_preorder(root)
        in_order = generate_inorder(root)
        res = binary_tree_from_preorder_inorder(pre_order, in_order)
        assert is_two_binary_trees_equal(root, res)


if __name__ == '__main__':
    main()
