# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # leetcode 26 删除排序数组中的重复项
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        slow, fast = 0, 1
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1

    # leetcode 80 删除排序数组中的重复项II
    def removeDuplicates2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        pre = nums[0]
        cnt = 1
        sum = 1
        for i in range(1, n):
            if nums[i] == pre:
                cnt += 1
                if cnt <= 2:
                    nums[sum] = nums[i]
                    sum += 1
            else:
                pre = nums[i]
                cnt = 1
                nums[sum] = nums[i]
                sum += 1
        return sum

    # leetcode 83 删除链表中的重复元素
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            if head == None:
                return head

            slow, fast = head, head.next
            while fast is not None:
                if fast.val != slow.val:
                    slow = slow.next
                    slow.val = fast.val
                fast = fast.next
            slow.next = None
            return head

        # leetcode 82 删除链表中的重复元素II，将所有重复元素都去掉
        def deleteDuplicates2(self, head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            dummyHead = ListNode(0)
            dummyHead.next = head
            prev = dummyHead
            while prev and prev.next:
                curr = prev.next
                # 没有重复元素
                if curr.next is None or curr.val != curr.next.val:
                    prev = curr
                else:
                    while curr.next is not None and curr.val == curr.next.val:
                        curr = curr.next
                    prev.next = curr.next
            return dummyHead.next


