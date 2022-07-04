# -*- coding: utf-8 -*-

class Solution:
    # leetcode 76 最小覆盖子串
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        for i in t:
            need[i] = need.get(i, 0) + 1

        left = 0
        right = 0
        valid = 0
        start = 0
        minLen = len(s) + 1

        while right < len(s):
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            right += 1

            while valid == len(need):
                if right - left < minLen:
                    start = left
                    minLen = right - left
                l = s[left]
                left += 1
                if l in need:
                    window[l] -= 1
                    if window[l] < need[l]:
                        valid -= 1
        return '' if minLen == len(s) + 1 else s[start: start + minLen]

    # leetcode 438 找到字符串中所有的字母异位词
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need = {}
        window = {}
        for c in p:
            need[c] = need[c].get(c, 0) + 1

        left = 0
        right = 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            right += 1

            while valid == len(need):
                if right - left == len(p):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
        return res

    # leetcode 3 无重复字母的最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        need = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            need[c] = need.get(c, 0) + 1
            while need[c] > 1:
                d = s[left]
                left += 1
                need[d] -= 1
            res = max(res, right-left)
        return res

