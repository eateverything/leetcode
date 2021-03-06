# -*- coding:utf-8 -*-

'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        col = len(array[0])

        i = 0
        j = col - 1

        while i <= row-1 and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
