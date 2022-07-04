# -*- coding:utf-8 -*-

'''
发散思维能力
题目：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

# 方法一：使用内置函数，明显不是要考察的点
class Solution:
    def Add(self, num1, num2):
        return sum([num1, num2])


# 方法二：二进制加法,模拟十进制加法的操作
class Solution1:
    def Add(self, num1, num2):
        while num2 != 0:
            temp = num1^num2  # 两个数异或操作，相当于各位求和，不进位
            num2 = (num1&num2)<<1  # 这一步是计算进位的
            num1 = temp & 0xffffffff  # 如果temp超出范围2^32，及时纠正过来
        return num1 if num1 >> 31 == 0 else num1 - 4294967296  # 2^32 = 4294967296，这句话是处理num1为负数时用的


if __name__ == "__main__":
    print(-3 & 0xffffffff)