# -*- coding: utf-8 -*-

# leetcode 887 鸡蛋掉落

class Solution(object):
    # 方法一：超时
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        memo = dict()
        def dp(K, N):
            if N == 0:
                return 0
            if K == 1:
                return N
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            for i in range(1, N+1):
                res = min(res, max(dp(K, i-1), dp(K-1, N-i)) + 1)
            memo[(K, N)] = res
        return dp(K, N)

    def superEggDrop2(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        memo = dict()
        def dp(K, N):
            if N == 0:
                return 0
            if K == 1:
                return N
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[(K, N)] = res
            return res
        return dp(K, N)

    def superEggDrop3(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0] * (N+1) for _ in range(K+1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        return m