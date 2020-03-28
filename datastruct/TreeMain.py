#! /usr/bin/python
# -*- encoding: utf-8 -*-


# 二叉搜索树：
# 1. 左子树上所有节点的值均小于它的根节点的值
# 2. 右子树上所有节点的值均大于它的根节点的值
# 3. Recursively, 左右子树也分别为二叉查找树
def is_valid_bst(root):
    """
    验证给定的二叉树为二叉搜索树
    LeetCode: 98
    :type root: TreeNode
    :rtype: bool
    """
    return order(root)


def order(root, path):
    """
    中序遍历，得到的结果是有序的，说明是二叉搜索树
    :type root: TreeNode
    :type path: list
    :return:
    """
    if not root:
        return True
    flag = order(root.left, path)
    if not flag:
        return False
    if path.pop() >= root.val:
        return False
    path.append(root.val)
    flag = order(root.right, path)
    if not flag:
        return False

    return True


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
