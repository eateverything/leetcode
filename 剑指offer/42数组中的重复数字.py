# -*- coding:utf-8 -*-

'''
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
'''

# 方案一，需要额外O(n)的空间
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        counter = {}
        flag = False
        for i in numbers:
            if i not in counter.keys():
                counter[i] = 1
            else:
                flag = True
                duplication[0] = i
                break
        return flag


# 方案二，不需要额外的空间
class Solution1:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            if numbers[i] != i:
                temp = numbers[numbers[i]]
                if temp == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = temp
        return False
