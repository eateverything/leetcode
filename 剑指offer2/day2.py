# -*- coding: utf-8 -*-

'''
1.用两个栈实现队列
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# 维护两个栈stackA和stackB，push操作时只需插入stackA
# pop操作时，若stackB中有元素，直接pop()，若stackB为空，则将stackA中的元素全部放进stackB中
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        self.stackA.append(node)
    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


'''
2.旋转数组中的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
# 从头到尾两两相邻元素进行比较进行，如果前面一个元素大于后面一个元素，则返回后面一个元素。
# 如果从头到尾都没有满足条件的元素，则返回第一个元素。
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]


'''
3.斐波那契数列
'''
class Solution:
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        a = b = 1
        for i in range(2, n):
            a, b = b, a+b
        return b


'''
4.跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''
class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        memo = [0] * (number+1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        for i in range(3, number + 1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[-1]


'''
5.变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
    def jumpFloorII(self, number):
        if number <= 2:
            return number
        memo = [1] * (number+1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        for i in range(3, number + 1):
            for j in range(1, i):
                memo[i] += memo[i-j]
        return memo[-1]


'''
6.矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        memo = [1] * (number+1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        for i in range(3, number + 1):
            for j in range(1, i):
                memo[i] += memo[i-j]
        return memo[-1]
