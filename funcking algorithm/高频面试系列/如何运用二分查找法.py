# -*- coding: utf-8 -*-

class Solution:
    # leetcode 875 爱吃香蕉的珂珂
    def minEatingSpeed(self, piles: list[int], H: int) -> int:
        def isCanFinish(piles, speed, H):
            time = 0
            for n in piles:
                time += n // speed
                if n % speed != 0:
                    time += 1
            return time <= H

        left = 1 # 最小速度
        max_n = 0
        for n in piles:
            max_n = max(max_n, n)
        right = max_n
        while left < right:
            mid = (left + right) // 2
            if isCanFinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left

    # leetcode 1011 D天内运输货物的能力
    def shipWithinDays(self, weights: list[int], D: int) -> int:
        def isCanFinish(weights, D, cap):
            i = 0
            for day in range(D):
                maxCap = cap
                while maxCap - weights[i] >= 0:
                    maxCap -= weights[i]
                    i += 1
                    if i == len(weights):
                        return True
            return False

        max_n = 0
        sum_n = 0
        for n in weights:
            max_n = max(max_n, n)
            sum_n += n
        left = max_n  #最小的装载能力为最大货物的重量，不然根本上不了船
        right = sum_n
        while left < right:
            mid = (left + right) // 2
            if isCanFinish(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return left