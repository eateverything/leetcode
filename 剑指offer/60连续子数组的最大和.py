# -*- coding:utf-8 -*-

'''
题目：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常
需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望
旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他
忽悠住？(子向量的长度至少是1)
'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        length = len(array)
        if length == 0:
            return 0
        if length == 1:
            return array[0]

        memo = []  # 用于存储第i个数时最大和
        memo.append(array[0])
        for i in range(1, length):
            memo.append(max(array[i], memo[i-1]+array[i]))

        max_value = -100000000
        for i in range(length):
            if max_value < memo[i]:
                max_value = memo[i]
        return max_value