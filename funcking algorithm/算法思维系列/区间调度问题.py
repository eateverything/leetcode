# -*- coding: utf-8 -*-

import functools

class Solution:
    # leetcode 56 合并区间
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        lastInterval = intervals[0]
        for interval in intervals:
            if lastInterval[1] >= interval[0]:
                lastInterval[1] = max(interval[1], lastInterval[1])
            else:
                res.append(lastInterval)
                lastInterval = interval
        res.append(lastInterval)
        return res

    def merge2(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]
            if last[1] >= cur[0]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)
        return res

    # leetcode 986 区间列表的交集
    def intervalIntersection(self, A, B):
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            a1 = A[i][0]
            a2 = A[i][1]
            b1 = B[j][0]
            b2 = B[j][1]
            if b1 <= a2 and a1 <= b2:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res

    # leetcode 354 俄罗斯套娃信封问题
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        def cmp(o1, o2):
            if o1[0] == o2[0]:
                return o2[1] - o1[1]
            else:
                return o1[0] - o2[0]
        envelopes = sorted(envelopes, key=functools.cmp_to_key(cmp))
        print(envelopes)
        height = []
        for i in range(n):
            height.append(envelopes[i][1])
        return self.lengthOfLIS(height)

    def lengthOfLIS(self, nums):
        piles = 0
        n = len(nums)
        top = [0] * n
        for i in range(n):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid + 1
            if left == piles:
                piles += 1
            top[left] = poker
        return piles


if __name__ == "__main__":
    nums = [[5, 4], [6, 4], [6, 7], [2, 3]]
    func = Solution()
    print(func.maxEnvelopes(nums))