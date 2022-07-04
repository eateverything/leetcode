# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # leetcode 198 打家劫舍
    def rob1(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n+2)
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        return dp[0]

    # leetcode 213 打家劫舍II，环形房屋
    def rob2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            return max(self.robRange(nums, 0, n-1), self.robRange(1, n))

    def robRange(self, nums, start, end):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[n-1] = nums[end-1]
        for i in range(n-2, start-1, -1):
            dp[i] = max(dp[i+1], nums[i]+(0 if i+2>=end else dp[i+2]))
        return dp[start]

    # leetcode 337 大家劫舍III
    def rob(self, root: TreeNode) -> int:
        def dp(root):
            if root is None:
                return [0, 0]
            left = dp(root.left)
            right = dp(root.right)
            rob = root.val + left[0] + right[0]
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            return [not_rob, rob]
        res = dp(root)
        return max(res[0], res[1])
