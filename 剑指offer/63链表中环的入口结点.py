# -*- coding:utf-8 -*-

'''
题目：一个链表中包含环，请找出该链表的环的入口结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        slow = pHead.next
        fast = pHead.next.next
        while slow != fast:
            if fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next
            else:
                return None
        fast = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast