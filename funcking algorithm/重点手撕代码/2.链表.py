# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.successor = None

    # leetcode 206 反转链表
    # 非递归实现
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = next = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 递归实现
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last

    # leetcode 160 链表香交
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        p = headA
        q = headB

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

    # leetcode 141 环形链表
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # leetcode 142 环形链表2
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    # leetcode 21 合并两个有序链表
    # 方法1：非递归版本
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        pHead = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return pHead.next

    # 方法2：递归版本
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        mergeHead = None

        if l1.val <= l2.val:
            mergeHead = l1
            mergeHead.next = self.mergeTwoLists2(l1.next, l2)
        else:
            mergeHead = l2
            mergeHead.next = self.mergeTwoLists2(l1, l2.next)
        return mergeHead

    # 合并K个有序链表
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        result = None
        for list in lists:
            result = self.mergeTwoLists(result, list)
        return result

    # leetcode 25 k个一组反转链表
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        a = b = head
        for i in range(k):
            if b is None:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead

    # 反转从a到b
    def reverse(self, a, b):
        pre = None
        cur = next = a
        while cur != b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 反转链表II
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    # 反转链表前n个节点
    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# leetcode 138 复制带随机指针的链表
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.copyNode(head)
        self.copyRandom(head)
        return self.reconnectNode(head)

    # 复制每一个节点，放在原节点后边
    def copyNode(self, head):
        pHead = head
        while pHead:
            # 深拷贝节点
            pNode = Node(0)
            pNode.val = pHead.val
            pNode.next = pHead.next
            # 复制节点连接
            pHead.next = pNode
            pHead = pNode.next

    # 复制每一个随机节点，指向原节点的下一个节点，即复制出来的节点
    def copyRandom(self, head):
        pHead = head
        while pHead:
            pNodeRandom = pHead.next
            if pHead.random is not None:
                pNodeRandom.random = pHead.random.next
            pHead = pNodeRandom.next

    # 拆分成原链表和复制链表
    def reconnectNode(self, head):
        pHead = head
        pCloneHead = pCloneNode = pHead.next
        pHead.next = pCloneNode.next
        pHead = pCloneNode.next
        while pHead:
            pCloneNode.next = pHead.next
            pCloneNode = pHead.next
            pHead.next = pCloneNode.next
            pHead = pCloneNode.next
        return pCloneHead




