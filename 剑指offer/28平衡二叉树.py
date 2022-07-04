# -*- coding:utf-8 -*-

'''
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

'''
平衡二叉树：平衡二叉搜索树（Balanced Binary Tree）具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值
不超过1，并且左右两个子树都是一棵平衡二叉树。
思路：如果二叉树的每个节点的左子树和右子树的深度不大于1，它就是平衡二叉树。
先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        depth1 = self.getDepth(pRoot.left)
        depth2 = self.getDepth(pRoot.right)
        if abs(depth1 - depth2) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def getDepth(self, root):
        if not root:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1