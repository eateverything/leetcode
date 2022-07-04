# -*- coding:utf-8 -*-

'''
题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
'''


class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        num = []
        numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in numbers.keys():
                num.append(numbers[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0
        ans = 0
        for i in num:
            ans = ans * 10 + i
        if s[0] == '-':
            ans = 0 - ans
        return ans