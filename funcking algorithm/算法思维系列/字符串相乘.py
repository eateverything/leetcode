# -*- coding: utf-8 -*-

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum = mul + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10

        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        s = ''
        for j in range(i, len(res)):
            s += str(res[j])
        return '0' if s == '' else s