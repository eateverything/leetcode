# -*- coding: utf-8 -*-

'''
1.二维数组中的查找
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        col = len(array[0])

        i = 0
        j = col - 1

        while i < row and j >=0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i += 1
            else:
                j -= 1
        return False


'''
2.从尾到头打印链表
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 使用栈从头到尾push链表的元素，然后pop所有的元素到一个list中并返回
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        p = listNode
        res = []
        stack = []
        while p:
            stack.append(p.val)
            p = p.next
        for i in range(len(stack)-1, -1, -1):
            res.append(stack[i])
        return res


'''
3.重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 根据前序遍历的结果，对于输入的遍历序列，第一个数一定是根结点，那么我们去中序遍历的结果中找到该根节点，
# 中序遍历结果中根结点左边的是左子树的节点，右边的是右子树的节点，这样很容易使用递归的思路实现二叉树的重建。
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None

        root = TreeNode(pre[0])
        i = 0
        while i < len(tin):
            if tin[i] == root.val:
                break
            i += 1
        index = i
        root.left = self.reConstructBinaryTree(pre[1: index+1], tin[: index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root

