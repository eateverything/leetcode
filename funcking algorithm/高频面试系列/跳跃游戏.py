# -*- coding: utf-8 -*-


class Solution:
    # leetcode 55 跳跃游戏
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        farest = 0
        for i in range(n-1):
            farest = max(farest, i+nums[i])
            if farest <= i:
                # 永远跳不过i这里
                return False
        return farest >= n-1

    # leetcode 45 跳跃游戏II
    # 解法一：相当于选择相邻两次能跳最远的组合
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        range = 1
        count = 0
        next = 0
        i = 1
        while range < n:
            if i <= range:
                # 相当于在当前一跳的范围内选择两跳内最远的
                next = max(next, i+nums[i-1])
                i += 1
            else:
                count += 1
                range = next
        return count

    # 解法二：寻找最优潜质的跳跃，两个解法好像一样，就是一样的，hahah
    def jump2(self, nums: list[int]) -> int:
        n = len(nums)
        jump = 0
        farest = 0
        end = 0
        for i in range(n-1):
            farest = max(farest, i+nums[i])
            if end == i:
                jump += 1
                end = farest
        return jump

