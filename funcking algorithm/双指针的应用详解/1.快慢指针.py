# -*- coding: utf-8 -*-

'''
leetcode 141 环形链表
给定一个链表，判断链表是否有环
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False


'''
leetcode 142 环形链表II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        if slow is None or fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


'''
LeetCode 22 链表倒数第k个节点
'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head

        while k > 0:
            fast = fast.next
            k -= 1

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow