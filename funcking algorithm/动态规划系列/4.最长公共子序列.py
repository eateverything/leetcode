# -*- coding: utf-8 -*-


'''
leetcode 1143 最长公共子序列
'''
# 递归算法，超时
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(i, j):
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                # 找到一个，继续
                return dp(i-1, j-1) + 1
            else:
                # 谁长就听谁的
                return max(dp(i, j-1), dp(i-1, j))
        return dp(len(text1)-1, len(text2)-1)


# 动态规划，dp[i][j] 表示s[1,...,i] 和 s[i,...,j]的最长公共子序列
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


'''
动态规划之子序列问题模板
1.第一种思路模板是一个一维的dp数组,例如最长递增子序列问题
dp数组的含义：在子数组array[i,...,j]中，我们要求的子序列(最长回文串)的长度为dp[i][j]
int n = array.length;
int[] dp = new int[n];
for(int i=1;i<n;i++){
    for(int j=0;j<i;j++){
        dp[i] = 最值(dp[i], ...)
    }
}

2.第二种思路模板是一个二维的dp数组
dp数组的含义：在子数组array1[0,...,i]和子数组array2[0,...,j]中，公共子序列的长度为dp[i][j]
int n = array.length;
int[][] dp = new int[n][n];
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        if(s1[i]==s2[j]){
            dp[i][j] = df[i][j] + ...;
        }
        else{
            dp[i][j] = 最值(...)
        }
    }
}
'''

'''
leetcode 516 最长回文子序列，第二种解决思路
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]