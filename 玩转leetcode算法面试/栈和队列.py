# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 20有效的括号
    def isValid(self, s: str) -> bool:
        def leftOf(c):
            if c == ')':
                return '('
            elif c == ']':
                return '['
            else:
                return '{'

        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) > 0 and leftOf(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    # 102 二叉树的层序遍历
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            sz = len(q)
            tmp = []
            for i in range(sz):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(tmp)
        return res

    # 107二叉树的层序遍历II
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        res = []

        def dfs(root, depth):
            if root is None:
                return
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            if root.left:
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)

        dfs(root, 0)
        return res[::-1]

    # 103二叉树的锯齿形层序遍历
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        res = []
        stack1 = [(root, 0)]
        stack2 = []
        while len(stack1) > 0 or len(stack2) > 0:
            while len(stack1) > 0:
                tmp = stack1.pop()
                node1 = tmp[0]
                level1 = tmp[1]
                if level1 == len(res):
                    res.append([])
                res[level1].append(node1.val)
                if node1.left:
                    stack2.append((node1.left, level1+1))
                if node1.right:
                    stack2.append((node1.right, level1+1))
            while len(stack2) > 0:
                tmp = stack2.pop()
                node2 = tmp[0]
                level2 = tmp[1]
                if level2 == len(res):
                    res.append([])
                res[level2].append(node2.val)
                if node2.right:
                    stack1.append((node2.right, level2+1))
                if node2.left:
                    stack1.append((node2.left, level2+1))
        return res




