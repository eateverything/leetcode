# -*- coding: utf-8 -*-

import functools

class Solution:
    # leetcode 1288 删除被覆盖区间
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        def cmp(o1, o2):
            if o1[0] == o2[0]:
                return o2[1] - o1[1]
            return o1[0] - o2[0]

        intervals = sorted(intervals, key=functools.cmp_to_key(cmp))

        left = intervals[0][0]
        right = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            interval = intervals[i]
            # 被覆盖啦
            if left <= interval[0] and right >= interval[1]:
                res += 1
            # 相交但没覆盖，那就合并了吧
            elif right >= interval[0]:
                right = interval[1]
            # 完全不相交
            elif right < interval[0]:
                left = interval[0]
                right = interval[1]
        return len(intervals) - res

    # leetcode 56 合并区间
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            interval = intervals[i]
            last = res[-1]

            # 如果相交
            if last[1] >= interval[0]:
                last[1] = max(last[1], interval[1])
            # 不相交
            else:
                res.append(interval)
        return res

    # leetcode 986 区间列表的交集
    def intervalIntersection(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            a1 = A[i][0]; a2 = A[i][1]
            b1 = B[j][0]; b2 = B[j][1]
            if a1 <= b2 and b1 <= a2:
                res.append([max(a1, b1), min(a2, b2)])
            if a2 < b2:
                i += 1
            else:
                j += 1
        return res
