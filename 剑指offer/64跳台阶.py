# -*- coding:utf-8 -*-

'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

class Solution:
    def jumpFloor(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            res = [0, 1, 2]
            while len(res) <= number:
                res.append(res[-1] + res[-2])
        return res[-1]

