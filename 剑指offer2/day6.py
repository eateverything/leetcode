# -*- coding: utf-8 -*-

'''
1.两个链表的第一个公共结点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = pHead2 if not p1 else p1.next
            p2 = pHead1 if not p2 else p2.next
        return p1


'''
2.数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。
'''
# 使用两次二分查找，分别找到最后一次出现的位置和第一次出现的位置。
class Solution:
    def GetNumberOfK(self, data, k):
        if not data or k < data[0] or k > data[-1]:
            return 0
        first = self.getFirst(data, k)
        last = self.getLast(data, k)
        number = 0
        if first != -1:
            number = last - first + 1
        return number

    def getFirst(self, data, k):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if data[mid] == k:
                if mid == 0 or data[mid-1] != data[mid]:
                    return mid
                else:
                    right = mid - 1
            elif data[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def getLast(self, data, k):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if data[mid] == k:
                if mid == len(data)-1 or data[mid + 1] != data[mid]:
                    return mid
                else:
                    left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        return -1


'''
3.二叉树的深度
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用递归的思路实现
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1


'''
4.平衡二叉树
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
'''
# 使用递归的思路求解二叉树的深度。
# 定义一个新函数，用来求解二叉树的深度，如果左右子树的深度之差超过1，那么返回-1，代表不是平衡二叉树，否则，返回子树的深度。
class Solution:
    def IsBalanced_Solution(self, pRoot):
        _, isbalance = self.IsBalanced(pRoot)
        return isbalance

    def IsBalanced(self, pRoot):
        if not pRoot:
            return 0, True
        dleft, isleft = self.IsBalanced(pRoot.left)
        dright, isright = self.IsBalanced(pRoot.right)
        if isleft and isright:
            diff = abs(dleft - dright)
            if diff <= 1:
                return max(dleft, dright) + 1, True
            else:
                return  -1, False
        return -1, False


'''
5.数组中只出现一次的数字
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
# 这里的思路是根据要求的这两个数的异或之后最右边不为1的这一位进行划分，将数组分成两部分
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = 0
        for i in array:
            res ^= i
        splitBit = 1
        while splitBit & res == 0:
            splitBit = splitBit << 1
        res1 = 0
        res2 = 0
        for i in array:
            if i & splitBit == 0:
                res1 ^= i
            else:
                res2 ^= i
        return [res1, res2]


'''
6.和为s的连续正数序列
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        small = 1
        big = 2
        cumSum = small + big
        while small <= tsum/2:
            if cumSum == tsum:
                res.append(range(small, big+1))
                big = big + 1
                cumSum += big
            elif cumSum > tsum:
                cumSum -= small
                small += 1
            else:
                big += 1
                cumSum += big
        return res

