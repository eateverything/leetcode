# -*- coding:utf-8 -*-

'''
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
将输入数组转成字符串，利用cmp比较mn或者nm的大小，进行从小到大的排序
notes:
31ms
5596k
'''

import operator
from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        # python2 解法
        lmb = lambda x, y: int(str(x) + str(y)) - int(str(y) + str(x))
        # array = sorted(numbers, cmp=lmb) # python2
        array = sorted(numbers, key=cmp_to_key(lmb))  # python3,将比较函数转化
        return ''.join([str(i) for i in array])



print(Solution().PrintMinNumber([3, 32, 321]))

