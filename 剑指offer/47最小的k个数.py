# -*- coding:utf-8 -*-

'''
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

# 思路：这道题考察的一定是小顶堆
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        self.minHeap(tinput)
        result = []
        count = 0
        while count < k:
            result.append(tinput[0])
            tinput.pop(0)
            self.minHeap(tinput)
            count += 1
        return result

    def minHeap(self, alist):
        length = len(alist)
        if not alist or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index + 1] < alist[index]:
                        index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

