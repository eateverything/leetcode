# -*- coding: utf-8 -*-

class Solution:
    # leetcode 560 和为k的子数组
    # 超出时间限制
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        sum = [0] * (n+1)
        for i in range(n):
            sum[i+1] = sum[i] + nums[i]
        ans = 0
        for i in range(1, n):
            for j in range(0, i):
                if sum[i] - sum[j] == k:
                    ans += 1
        return ans

    # 优化算法，使用字典代替内层循环
    def subarraySum_better(self, nums: list[int], k: int) -> int:
        n = len(nums)
        preSum = {}
        preSum[0] = 1
        ans = 0
        sum_i = 0
        for i in range(0, n):
            sum_i += nums[i]
            sum_j = sum_i - k
            if sum_j in preSum:
                ans += preSum[sum_j]
            preSum[sum_i] = preSum.get(sum_i, 0) + 1
        return ans
