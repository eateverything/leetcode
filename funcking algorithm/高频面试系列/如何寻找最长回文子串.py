# -*- coding: utf-8 -*-


class Solution:
    # leetcode 5 最长回文子串，双指针，由中间向两边开花
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]

        res = ''
        for i in range(0, len(s)):
            res1 = palindrome(s, i, i)
            res2 = palindrome(s, i, i+1)
            res = res if len(res)>len(res1) else res1
            res = res if len(res)>len(res2) else res2
        return res

    # 动态规划解法，难道是马拉车？想太多
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[0] * n for _ in range(n)]
        maxLen = 1
        start = 0
        for gap in range(1, n):
            for i in range(0, n - gap):
                j = i + gap
                if gap <= 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = (dp[i + 1][j - 1] == 1)

                if dp[i][j] == 1 and maxLen < gap + 1:
                    maxLen = gap + 1
                    start = i
        return s[start: start + maxLen]

    # leetcode 516 最长回文子序列
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

