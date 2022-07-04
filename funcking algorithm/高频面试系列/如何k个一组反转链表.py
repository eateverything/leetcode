# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # leetcode 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        nxt = head
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    # 反转区间[a, b)之间的链表
    def reverse(self, a, b):
        pre = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    # leetcode 25 k个一组翻转链表
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        a = b = head
        for i in range(k):
            # 不足k个，不翻转
            if b is None:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead