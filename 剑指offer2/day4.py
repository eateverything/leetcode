# -*- coding: utf-8 -*-

'''
1.顺时针打印矩阵
'''
# 1、首先可以看到，第一圈的第一个元素是（0，0），第二圈是（1，1），所以我们可以找到左上角元素的规律
# 2、这样，我们可以循环的打印每一圈的值，不过要注意最后一圈的情况
# 3、打印第一行不会有问题
# 4、打印第一列，要保证最后一圈至少有两行
# 5、打印第二行，不仅要至少有两行，而且至少有两列
# 6、打印第二列，我们至少要有三行，两列才可以
class Solution:
    def __init__(self):
        self.res = []
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while rows > start*2 and cols > start*2:
            self.printOneCircle(matrix, rows, cols, start)
            start += 1
        return self.res

    def printOneCircle(self, matrix, rows, cols, start):
        endrow = rows - start - 1
        endcol = cols - start - 1
        for i in range(start, endcol+1):
           self.res.append(matrix[start][i])
        if endrow > start:
            for i in range(start+1, endrow+1):
                self.res.append(matrix[i][endcol])
        if endrow > start and endcol > start:
            for i in range(endcol-1, start-1, -1):
                self.res.append(matrix[endrow][i])
        if endcol > start and (endrow - start) > 1:
            for i in range(endrow-1, start, -1):
                self.res.append(matrix[i][start])


'''
2.包含min函数的栈
'''
# min栈与栈保持同步
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        self.stack.append(node)
        if self.minstack == [] or node < self.minstack[-1]:
            self.minstack.append(node)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
        else:
            return None

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def min(self):
        if self.minstack:
            return self.minstack[-1]
        else:
            return None


'''
3.栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
# 模拟两个栈的压入、弹出
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        while popV:
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            elif stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            else:
                return False
        return True


'''
4.从上往下打印二叉树
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


'''
5.二叉搜索树的后续遍历结果
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
'''
# 递归进行判断，如果序列的长度小于等于2，那么一定是后序遍历的结果，否则根据BST和后序遍历的性质，
# 遍历结果的最后一个一定是根节点，那么序列中前面一部分小于根节点的数是左子树，后面一部分是右子树，递归进行判断。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.VerifySubSquenceOfBST(sequence)

    def VerifySubSquenceOfBST(self, sequence):
        if len(sequence) < 3:
            return True

        flag = sequence[-1]
        index = 0
        while sequence[index] < flag:
            index += 1

        j = index
        while j < len(sequence) - 1:
            if sequence[j] > flag:
                j += 1
            else:
                return False
        return self.VerifySubSquenceOfBST(sequence[: index]) and self.VerifySubSquenceOfBST(sequence[index: -1])


'''
6.二叉树中和为某一值的路径
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
# 定义一个子函数，输入的是当前的根节点、当前的路径以及还需要满足的数值，同时在子函数中运用回溯的方法进行判断。
class Solution:
    def __init__(self):
        self.res = []

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        self.SubPath(root, [], expectNumber)
        return self.res

    def SubPath(self, root, path, number):
        if root.left is None and root.right is None:
            if number == root.val:
                self.res.append(path + [root.val])
            return
        if root.left:
            self.SubPath(root.left, path + [root.val], number - root.val)
        if root.right:
            self.SubPath(root.right, path + [root.val], number - root.val)








