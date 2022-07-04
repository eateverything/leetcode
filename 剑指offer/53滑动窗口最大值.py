# -*- coding:utf-8 -*-

'''
题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及
滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的
滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

# 思路一：正常暴力解法，但是考察点不能这么简单吧
class Solution:
    def maxInWindows(self, num, size):
        if size <= 0 or len(num) < size:
            return []
        ans = []
        length = len(num)
        for i in range(0, length-size+1):
            current = max(num[i: i+size])
            ans.append(current)
        return ans


# 思路二：使用双端队列
class Solution1:
    def maxInWindows(self, num, size):
        if size <= 0 or len(num) < size:
            return []
        res = []  # 这个list存储结果
        queue = []  # 这个list充当双端队列，保存的是数组中数字的索引，为什么保存索引？
        length = len(num)
        for i in range(0, length):
            while len(queue) and num[queue[-1]] <= num[i]: # 保证双端队列是逆序排列
                queue.pop()
            while len(queue) and i-queue[0]+1 > size:  # 保存索引是为了方便判断对头是否还在滑动窗口内
                queue.pop(0)
            queue.append(i)
            if i+1 >= size:
                res.append(num[queue[0]])
        return res