# -*- coding: utf-8 -*-

class Solution():
    # 下一个更大元素
    def nextGreaterElement(self, nums):
        n = len(nums)
        stack = []
        ans = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i]:
                stack.pop()
            num = -1 if len(stack) <= 0 else stack[-1]
            ans.insert(0, num)
            stack.append(nums[i])
        return ans

    # leetcode 739 每日温度
    def dailyTemperatures(self, T: list[int]) -> list[int]:
        n = len(T)
        stack = []
        ans = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            index = 0 if len(stack) <= 0 else stack[-1] - i
            ans.insert(0, index)
            stack.append(i)
        return ans

    # leetcode 503 下一个更大元素II ，循环数组
    def nextGreaterElementsi(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stack = []
        ans = [0] * n
        for i in range(2 * n - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i % n]:
                stack.pop()
            ans[i % n] = -1 if len(stack) <= 0 else stack[-1]
            stack.append(nums[i % n])
        return ans

