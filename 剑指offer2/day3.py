# -*- coding: utf-8 -*-

'''
1. 二进制中1的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
# n和n-1的与运算，结果是将n的最后一位变成了0
# 要注意n<0时的补码表示
class Solution:
    def NumberOf1(self, n):
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count


'''
2. 链表中倒数第K个节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        p1 = p2 = head
        while k > 1:
            if p2.next is not None:
                p2 = p2.next
                k -= 1
            else:
                return None
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        return p1


'''
3. 反转链表
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead

        dummy = ListNode(-1)
        dummy.next = pHead
        p = pHead.next
        while p:
            q = p
            p = p.next
            q.next = dummy.next
            dummy.next = q
        pHead.next = None
        return dummy.next


'''
4. 合并两个排序链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        dummy = ListNode(0)
        pHead = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                dummy.next = pHead1
                pHead1 = pHead1.next
            else:
                dummy.next = pHead2
                pHead2 = pHead2.next
            dummy = dummy.next
        if pHead1:
            dummy.next = pHead1
        if pHead2:
            dummy.next = pHead2
        return pHead.next


'''
5.树的子结构
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.isSubtree(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSubtree(pRoot1.left, pRoot2.left) and self.isSubtree(pRoot1.right, pRoot2.right)


'''
6.二叉树的镜像
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


