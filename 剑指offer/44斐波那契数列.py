# -*- coding:utf-8 -*-

'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

class Solution:
    def Fibonacci(self, n):
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]


class Solution1:
    def Fibonacci(self, n):
        if n < 2:
            return n
        count = 2
        a, b = 0, 1
        while count <= n:
            b, a = a+b, b
            count += 1
        return b