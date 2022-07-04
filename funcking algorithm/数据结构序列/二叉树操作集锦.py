# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode 100 相同的树
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# leetcode 98 验证二叉树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)

    def isValid(self, root, min, max):
        if root is None:
            return True
        if min is not None and root.val <= min.val:
            return False
        if max is not None and root.val >= max.val:
            return False
        return self.isValid(root.left, min, root) and self.isValid(root.right, root, max)

# leetcode 701 二叉搜索树的插入操作
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root

# leetcode 450 删除二叉搜索树的结点
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, node):
        while node.left is not None:
            node = node.left
        return node

# leetcode 226 翻转二叉树
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# leetcode 116 填充每个节点的下一个右侧节点指针
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connectNode(node1, node2):
            if node1 is None or node2 is None:
                return
            node1.next = node2
            connectNode(node1.left, node1.right)
            connectNode(node2.left, node2.right)
            # 夸父节点连接,本题考察的重点
            connectNode(node1.right, node2.left)

        if root is None:
             return None

        connectNode(root.left, root.right)
        return root


# leetcode 114 二叉树展开为链表
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root
        while p.right is not None:
            p = p.right
        p.right = right

        return root


