# -*- coding:utf-8 -*-

'''
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
思路：1. 根据旧链表创建新链表，不去管随机的那个指针
     2. 根据旧链表中的随机指针，创建新链表中的随机指针
     3. 从旧链表中拆分得到新链表
'''


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNode(pHead)
        self.CloneRandomNode(pHead)
        return self.ReconnecctNodes(pHead)

    # 复制节点，每个复制节点放在原节点后边
    def CloneNode(self, pHead):
        pNode = pHead
        while pNode:
            # 复制节点
            pClone = RandomListNode(0)
            pClone.label = pNode.label
            pClone.next = pNode.next
            # 放在原节点后边
            pNode.next = pClone
            pNode = pClone.next

    # 复制随机节点，复制节点的随机指针指向原随机指针指向节点的下一个节点，即是要指向的复制节点
    def CloneRandomNode(self, pHead):
        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next
            pNode = pClone.next

    # 拆分链表，分为旧链表和新链表
    def ReconnecctNodes(self, pHead):
        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pCloneNode.next
        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pCloneNode.next
        return pCloneHead




