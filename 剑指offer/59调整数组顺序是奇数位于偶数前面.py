# -*- coding:utf-8 -*-

'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# 思路一：使用额外空间，两个数组分别存储奇数和偶数
class Solution:
    def reOrderArray(self, array):
        alist = []
        blist = []
        for i in array:
            if i % 2 != 0:
                alist.append(i)
            else:
                blist.append(i)
        return alist + blist


# 思路二：不使用额外空间，我觉得这才是这道题考查的点
class Solution1:
    def reOrderArray(self, array):
        for i in range(len(array)):
            if array[i] % 2 == 0:
                continue
            else:
                j = i
                while j-1 >= 0 and array[j-1] % 2 == 0:
                    array[j], array[j-1] = array[j-1], array[j]
                    j -= 1
        return array