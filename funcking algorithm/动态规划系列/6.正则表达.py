# -*- coding: utf-8 -*-

'''
leetcode 10 正则表达是匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
'''
# 暴力递归
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        first = bool(s) and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:])) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])


# 带备忘录的递归
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            first = i < len(s) and p[j] in (s[i], '.')
            if j <= len(p) - 2 and p[j+1] == '*':
                ans = dp(i, j+2) or (first and dp(i+1, j))
            else:
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)