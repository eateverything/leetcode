# -*- coding: utf-8 -*-

class Solution:
    # leetcode 10 正则表达式匹配
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        # 解法一
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            # 判断前一个字母是否匹配
            first = i < len(s) and p[j] in ('.', s[i])
            # 如果下一个匹配字符是'*'
            if j <= len(p) - 2 and p[j+1] == '*':
                # 要么匹配0次，要么匹配n次
                ans = dp(i, j+2) or (first and dp(i+1, j))
            else:
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)

    # 解法二，比较麻烦的写法
    def isMatch2(self, s: str, p: str) -> bool:
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            if i == len(s):
                if (len(p)-j) % 2 == 1:
                    return False
                for m in range(j, len(p)-1, 2):
                    if p[m+1] != '*':
                        return False
                return True
            # 如果前一个字符匹配的话
            if s[i] == p[j] or p[j] == '.':
                # 如果下一个匹配是'*'
                if j < len(p) - 1 and p[j+1] == '*':
                    # 匹配0个或者n个
                    res = dp(i, j+2) or dp(i+1, j)
                else:
                    res = dp(i+1, j+1)
            else:
                if j < len(p) - 1 and p[j+1] == '*':
                    # 匹配0个或者n个
                    res = dp(i, j+2)
                else:
                    res = False
            memo[(i, j)] = res
            return res

    # leetcode 410 分割数组的最大值
    def splitArray(self, nums: list[int], m: int) -> int:
        # 辅助函数，当确定子数组和最大为maxV时，至少可以分成多少个子数组
        def split(nums, maxV):
            count = 1
            sum = 0
            for num in nums:
                if sum + num > maxV:
                    count += 1
                    sum = num
                else:
                    sum += num
            return count

        lo = self.getMax(nums)
        hi = self.getSum(nums) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            n = split(nums, mid)
            if n == m:
                hi = mid
            elif n < m:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def getMax(self, nums):
        res = 0
        for num in nums:
            res = max(res, num)
        return res

    def getSum(self, nums):
        sum = 0
        for num in nums:
            sum += num
        return sum

    # leetcode 887 高楼扔鸡蛋
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # 状态：鸡蛋个数，选择：在那一层丢鸡蛋
        memo = dict()
        def dp(K, N):
            if N == 0:
                return 0
            if K == 1:
                return N
            if (K, N) in memo:
                return memo[(K, N)]

            lo, hi = 1, N
            res = float('INF')
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K-1, mid-1)
                not_broken = dp(K, N-mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken+1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken+1)
            memo[(K, N)] = res
            return res
        return dp(K, N)

    # 经典动态规划解法
    def superEggDrop2(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # dp[k][m]表示当前有k个鸡蛋，最多可以扔m次，最坏情况可以测试多少层高的楼
        # dp[k][m]的上界是dp[k][m]==N
        dp = [[0] * (N+1) for _ in range(K+1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        return m


