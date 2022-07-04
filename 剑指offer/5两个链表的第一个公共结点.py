# -*- coding:utf-8 -*-

'''
题目：输入两个链表，找出它们的第一个公共结点
'''

'''
思路：共同节点，意味着从共同节点开始之后所有的节点数都是相同的，这是链表，只要有一个共同节点，那么之后所有的指向
也是重复的。先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后
两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        firstLength = self.getLength(pHead1)
        secondLength = self.getLength(pHead2)
        lengthDiff = abs(firstLength - secondLength)

        if firstLength <= secondLength:
            longList = pHead2
            shortList = pHead1
        else:
            longList = pHead1
            shortList = pHead2
        while lengthDiff > 0:
            longList = longList.next
            lengthDiff -= 1
        while shortList != None and longList != None and longList != shortList:
            shortList = shortList.next
            longList = longList.next
        return longList


    def getLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length


# 方法二
class Solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = pHead2 if not p1 else p1.next
            p2 = pHead1 if not p2 else p2.next
        return p1