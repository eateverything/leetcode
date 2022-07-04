# -*- coding: utf-8 -*-

class Solution:
    # leetcode 42 接雨水，双指针解题
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0
        n = len(height)
        left = 0
        right = n-1
        lmax = height[0]
        rmax = height[n-1]
        ans = 0
        while left <= right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            if lmax < rmax:
               ans += lmax - height[left]
               left += 1
            else:
                ans += rmax - height[right]
                right -= 1
        return ans
