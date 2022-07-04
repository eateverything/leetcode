# -*- coding:utf-8 -*-

'''
考察：代码的鲁棒性

题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：递归版本
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        mergeHead = None
        if pHead1.val <= pHead2.val:
            mergeHead = pHead1
            mergeHead.next = self.Merge(pHead1.next, pHead2)
        elif pHead1.val > pHead2.val:
            mergeHead = pHead2
            mergeHead.next = self.Merge(pHead1, pHead2.next)
        return mergeHead


# 方法二：非递归版本，使用虚拟链表头
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        dummy = ListNode(0)
        pHead = dummy

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                dummy.next = pHead1
                pHead1 = pHead1.next
            elif pHead1.val > pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            dummy = dummy.next
        if pHead1:
            dummy.next = pHead1
        elif pHead2:
            dummy.next = pHead2
        return pHead.next