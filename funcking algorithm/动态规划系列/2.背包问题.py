# -*- coding: utf-8 -*-

'''
1.经典0-1背包问题
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两 个属性。其中第 i 个物品的重量为 wt[i] ，价值为 val[i] ，
现在让你用 这个背包装物品，最多能装的价值是多少?
'''
# 套路：
# 第一步确定状态：可选择的物品与背包的容量
# 第二步确定选择：装进背包和不装进背包
# 第三部：明确dp数组，因为有两种状态，所以dp是二维数组，dp[i][w]表示放进i个物品，重量是w时背包的价值
# 第四部确定状态转移方程：
# 1）物品i不放进背包：dp[i][w] = dp[i-1][w]，继承上一个价值
# 2）物品i放进背包：dp[i][w] = dp[i-1][w-wt[i-1]] + val[i-1]
# 3）所以 dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])


def knapsack(W, N, wt, val):
    # dp = [[0] * (W+1)] * (N+1)  # 这种定义方法在python中是错误的
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(1, W+1):
            if w - wt[i-1] < 0:
                # 背包没有容量了
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])
    return dp[N][W]


'''
leetcode 518 零钱兑换2
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
'''
# dp[i][j] 表示使用前i种硬币，凑出面值j有dp[i][j]种方法
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[0] * (amount+1)] * (len(coins)+1)
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount]

    def change2(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]


'''
子集背包问题
leetcode 416 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等
'''
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_arr = sum(nums)
        if sum_arr % 2 != 0:
            return False
        target = sum_arr // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(n):
            for j in range(target, -1, -1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j - nums[i - 1]] or dp[j]
        return dp[target]

    def canPartition2(self, nums: list[int]) -> bool:
        sum_arr = sum(nums)
        if sum_arr % 2 != 0:
            return False
        target = sum_arr // 2
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            for j in range(1, target+1):
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]










