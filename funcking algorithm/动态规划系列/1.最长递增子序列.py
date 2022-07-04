# -*- coding: utf-8 -*-


'''
leetcode 300 最长上升子序列
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)  # dp[i]表示以nums[i]结尾的最长上升子序列
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for num in dp:
            res = max(res, num)
        return res


'''
leetcode 300 最长上升子序列 二分查找算法
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        top = [0] * len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]
            left = 0
            right = piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] < poker:
                    left = mid + 1
                elif top[mid] > poker:
                    right = mid
                else:
                    right = mid
            # 没地方放就新建一堆
            if left == piles:
                piles += 1
            top[left] = poker
        return piles
