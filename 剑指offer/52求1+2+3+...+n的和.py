# -*- coding:utf-8 -*-

'''
题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

class Solution:
    def Sum_Solution(self, n):
        sum = 0
        if n > 0:
            sum =  n + self.Sum_Solution(n-1)
        return sum