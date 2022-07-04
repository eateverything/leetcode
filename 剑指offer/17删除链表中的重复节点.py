# -*- coding:utf-8 -*-

'''
题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None:
            return

        preHead = None
        pNode = pHead

        while pNode != None:
            needDelete = False
            nextNode = pNode.next
            if nextNode != None and nextNode.val == pNode.val:
                needDelete = True
            if needDelete == False:
                preHead = pNode
                pNode = pNode.next
            else:
                pToBeDel = pNode
                nodeval = pNode.val
                while pToBeDel != None and pToBeDel.val == nodeval:
                    pToBeDel = pToBeDel.next
                if preHead == None:
                    pHead = pToBeDel
                    pNode = pToBeDel
                else:
                    preHead.next = pToBeDel
                    pNode = preHead
        return pHead
