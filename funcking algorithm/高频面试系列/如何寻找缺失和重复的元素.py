# -*- coding: utf-8 -*-

class Solution:
    # leetcode 268 缺失数字
    # 使用异或，相同数字异或为0
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        res ^= n
        for i in range(n):
            res ^= (i ^ nums[i])
        return res

    # 方法二，索引与元素相减求和，这个和就是缺失的数字
    def missingNumber2(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        res += n
        for i in range(n):
            res += (i - nums[i])
        return res

    # leetcode 645 错误的集合,寻找缺失和重复的元素
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dup = -1
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
        return [dup, missing]
