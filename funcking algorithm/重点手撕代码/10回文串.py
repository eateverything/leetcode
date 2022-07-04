# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # leetcode 5 最长回文子串
    # 方法一：双指针技巧
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ''
        for i in range(0, len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    # 方法二：动态规划
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        # dp[i][j] 表示s[i,...,j]是否是回文子串
        dp = [[0] * n for _ in range(n)]
        start = 0
        maxLen = 1
        for gap in range(1, n):
            for i in range(0, n - gap):
                j = i + gap
                if gap <= 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = (dp[i + 1][j - 1] == 1)
                if dp[i][j] == 1 and maxLen < gap + 1:
                    start = i
                    maxLen = gap + 1
        return s[start: start + maxLen]

    # leetcode 516 最长回文子序列
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j]表示s[i,...j]最长回文子序列长度
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

    # leetcode 234 回文链表
    # 方法一：快慢指针
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            pre = None
            cur = next = head
            while cur is not None:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        slow = reverse(slow)
        while slow is not None:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

    # 方法二：类似二叉树递归
    def __init__(self):
        self.left = None

    def isPalindrome(self, head: ListNode) -> bool:
        def traverse(right):
            if right is None:
                return True
            res = traverse(right.next)
            res = res and (self.left.val == right.val)
            self.left = self.left.next
            return res

        self.left = head
        return traverse(head)

    # leetcode 1312 让字符串成为回文串的最少插入次数
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1]




