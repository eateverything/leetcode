# -*- coding: utf-8 -*-

import functools

'''
leetcode 435 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
'''
class Solution:
    def eraseOverlapIntervals(self, intervals):
        n = len(intervals)
        if n == 0:
            return 0

        def cmp(a, b):
            if a[1] < b[1]:
                return -1
            if a[1] > b[1]:
                return 1
            return 0

        intervals = sorted(intervals, key=functools.cmp_to_key(cmp))
        print(intervals)

        count = 1
        x_end = intervals[0][1]
        for interval in intervals:
            start = interval[0]
            if start >= x_end:
                count += 1
                x_end = interval[1]
        return n - count

    #区间合并
    def merge(self, intervals):
        n = len(intervals)
        if n < 2:
            return intervals

        def cmp(o1, o2):
            if o1[0] < o2[0]:
                return -1
            if o1[0] > o2[0]:
                return 1
            return 0
        intervals = sorted(intervals, key=functools.cmp_to_key(cmp))
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            print(res)
            curr = intervals[i]
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)
        return res


    # 区间交集
    def intervalIntersection(self, A, B):
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            if b1 <= a2 and a1 <= b2:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    so = Solution()
    res = so.merge(intervals)
    print(res)