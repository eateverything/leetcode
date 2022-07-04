# -*- coding:utf-8 -*-

'''
题目：输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一：切片
class Solution:
    def FindKthToTail(self, head, k):
        res = []
        while head:
            res.append(head)
            head = head.next
        if len(res) < k or k < 1:
            return
        return res[-k]


# 方法二：前后指针
class Solution1:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        p1 = head
        p2 = head
        while k > 1:
            if p2.next is not None:
                p2 = p2.next
                k -= 1
            else:
                return None
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        return p1