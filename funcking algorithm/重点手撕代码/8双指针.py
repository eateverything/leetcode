# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # leetcode 26 删除排序数组中的重复元素
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        slow, fast = 0, 0
        while fast < n:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

    # leetcode 83 删除排序链表中的重复元素
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow, fast = head, head
        while fast is not None:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head

    # leetcode 27 移除元素
    def removeElement(self, nums: list[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

    # leetcode 283 移动零
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
