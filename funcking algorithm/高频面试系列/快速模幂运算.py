# -*- coding: utf-8 -*-

class Solution:
    # leetcode 372 超级次方
    # a^[1,5,6,4] = a^4 * (a^[1,5,6])^10
    # 求余：(a*b)%k = (a%k)(b%k)%k
    # a^b = a * a^(b-1) if b是计数 else a^b = (a^(b/2))^2
    def superPow(self, a: int, b: list[int]) -> int:
        def myPow(a, k):
            if k == 0:
                return 1
            a %= 1337
            if k % 2 != 0:
                return (a * myPow(a, k-1)) % 1337
            else:
                sub = myPow(a, k // 2)
                return (sub * sub) % 1337

        if len(b) == 0:
            return 1
        last = b.pop()
        part1 = myPow(a, last)
        part2 = myPow(self.superPow(a, b), 10)
        return (part1 * part2) % 1337