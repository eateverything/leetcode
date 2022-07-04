# -*- coding: utf-8 -*-

class Solution:
    # leetcode 1 两数之和
    # 方法1：使用字典
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i, num in enumerate(nums):
            index[num] = i

        for i in range(len(nums)):
            if (target-nums[i]) in index and index[target-nums[i]] != i:
                return [i, index[target-nums[i]]]
        return []

    # leetcode 167 两数之和2
    # 方法二：左右指针, 只对有序数组或不在乎元素顺序的情况时可用
    def twoSum_new(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return []