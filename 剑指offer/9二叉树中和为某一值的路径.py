# -*- coding:utf-8 -*-

'''
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

'''
思路：
递归先序遍历树， 把结点加入路径。使用列表结构存树结构
若该结点是叶子结点则比较当前路径和是否等于期待和，叶子节点说明该路径应该截止了
弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        result = []

        def FindPath2(root, path, currentNumber):
            currentNumber += root.val
            path.append(root)
            # 判断该结点是不是叶子结点
            flag = root.left == None and root.right == None
            if currentNumber == expectNumber and flag:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)
            # 不满足条件继续递归
            if currentNumber < expectNumber:
                if root.left:
                    FindPath2(root.left, path, currentNumber)
                if root.right:
                    FindPath2(root.right, path, currentNumber)

            # 找到一条路径或者到叶子结点之后，要回退到上一个父结点继续遍历
            path.pop()
        FindPath2(root, [], 0)
        return result
