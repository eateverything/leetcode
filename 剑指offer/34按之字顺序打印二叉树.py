# -*- coding:utf-8 -*-

'''
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        result, nodes = [], [pRoot]
        leftToright = True
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            if not leftToright:
                curStack.reverse()
            if curStack:
                result.append(curStack)
            nodes = nextStack
            leftToright = not leftToright
        return result
