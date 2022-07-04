# -*- coding: utf-8 -*-

class Solution:
    # leetcode 204 计数质数
    # 核心思想：一个数是质数，他的倍数就都不是质数
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count