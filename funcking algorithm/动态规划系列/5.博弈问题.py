# -*- coding: utf-8 -*-

'''
leetcode 877 石子游戏
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false
'''
class Solution:
    def stoneGame(self, piles):
        n = len(piles)
        dp = [[[0, 0]] * n for _ in range(n)]
        print(dp)
        # 为何一定要加这段代码
        for i in range(0, n):
            for j in range(i, n):
                dp[i][j] = [0, 0]

        for i in range(n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0

        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = l + i - 1
                # 先手拿左边
                left = piles[i] + dp[i+1][j][1]
                # 先手拿右边
                right = piles[j] + dp[i][j-1][1]
                # print(l, left, right)
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        return dp[0][n-1][0] - dp[0][n-1][1]


if __name__ == "__main__":
    piles = [3, 7, 2, 3]
    print(Solution().stoneGame(piles))