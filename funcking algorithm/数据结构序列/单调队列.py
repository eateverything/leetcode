# -*- coding: utf-8 -*-


# leetcode 239 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if nums is None or len(nums) < 2:
            return nums
        res = []
        deque = []
        for i in range(len(nums)):
            # 如果队列不为空，且达到了长度看，移除头部元素
            while len(deque) > 0 and deque[0] == i - k:
                deque.remove(deque[0])  # remove的参数是数值，不是索引
            # 保持队列有序
            while len(deque) > 0 and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res