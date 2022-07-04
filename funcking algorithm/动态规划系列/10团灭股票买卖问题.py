# -*- coding: utf-8 -*-

class Solution:
    # leetcode 121 买卖股票的最佳时机
    # 给定一个数组，它的第 i个元素是一支给定股票第i天的价格。
    # 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    # 注意：你不能在买入股票前卖出股票。
    def maxProfit_k_1(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]

    def maxProfit_k_2(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        curSum, maxSum = 0, 0
        for i in range(1, n):
            curSum = max(0, curSum + prices[i] - prices[i-1])
            maxSum = max(maxSum, curSum)
        return maxSum

    # leetcode 122 买卖股票的最佳时机II
    # 通用方法,无限次跟1次是没有太大区别的，有限次才特殊
    def maxProfit_k_inf(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

    # 核心思想，既然可以无限次交易，那么只有赚钱我就买卖
    def maxProfit_k_inf_new(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        maxSum = 0
        for i in range(1, n):
            if prices[i] - prices[i-1] > 0:
                maxSum += prices[i] - prices[i-1]
        return maxSum

    # leetcode 714 买卖股票最佳时机，含手续费
    # 无限次买卖，我就假设买入时有手续费
    def maxProfit_k_inf_with_fee(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[n - 1][0]

    # leetcode 309 买卖股票最佳时机，含冷冻期
    def maxProfit_k_inf_cold(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i > 2:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n - 1][0]

    # leetcode 123 买卖股票最佳时机III
    def maxProfit_k_2(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp_i10 = 0
        dp_i20 = 0
        dp_i11 = -prices[0]
        dp_i21 = -prices[0]
        for i in range(1, n):
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, -prices[i])
        return dp_i20

    # leetcode 188 买卖股票最佳时机IIII
    def maxProfit_k(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        if k > n // 2:
            return self.maxProfit_k_inf(prices)
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]

        for i in range(1, k+1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[n-1][k][0]


