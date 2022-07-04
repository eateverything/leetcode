# -*- coding: utf-8 -*-

'''
1.和为S的两个数字
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
# 由于是排好序的数组，因此对于和相等的两个数来说，相互之间的差别越大，那么乘积越小，
# 因此我们使用两个指针，一个从前往后遍历，另一个从后往前遍历数组即可。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        left = 0
        right = len(array) - 1
        while left < right:
            if array[left] + array[right] > tsum:
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                return [array[left], array[right]]
        return []


'''
2.扑克牌顺子
'''
# 分三步走
# 1、将数组排序
# 2、统计数组中0的个数，即判断大小王的个数
# 3、统计数组中相邻数字之间的空缺总数，如果空缺数小于等于大小王的个数，可以组成顺子，否则不行
# 注意到一点是，如果数组中出现了对子，那么一定是不可以组成顺子的。
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        zeros = 0
        while numbers[zeros] == 0:
            zeros += 1
        for i in range(zeros, len(numbers)-1):
            if numbers[i] == numbers[i+1] or (numbers[i+1] - numbers[i] - 1) > zeros:
                return False
            else:
                zeros -= (numbers[i+1] - numbers[i] - 1)
        return True


'''
3.不用加减乘除做加法
'''
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            res = (num1 ^ num2)
            num2 = (num1 & num2) << 1
            num1 = res & 0xffffffff
        return num1 if num1 >> 31 == 0 else num1 - 4294967296
