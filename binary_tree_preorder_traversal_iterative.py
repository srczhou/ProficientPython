#!/usr/bin/env python3

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def generate_preorder(tree):
    result = []
    def preorder_recursive(tree):
        if tree:
            result.append(tree.data)
            preorder_recursive(tree.left)
            preorder_recursive(tree.right)
    preorder_recursive(tree)
    return result


# right first, left second,  because stack is LIFO
def preorder_traversal(tree):
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result


def main():
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    res = preorder_traversal(tree)
    golden_res = generate_preorder(tree)
    print(res)
    print("***")
    print(golden_res)
    #assert res == golden_res


if __name__ == '__main__':
    main()
