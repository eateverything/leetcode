# -*- coding:utf-8 -*-

'''
题目：统计一个数字在排序数组中出现的次数。
'''

class Solution:
    def GetNumberOfK(self, data, k):
        number = 0
        if data is not None and len(data)>0:
            length = len(data)
            first = self.getFirst(data, k, 0, length-1)
            last = self.getLast(data, k , 0, length-1)
            if first != -1:
                number = last - first + 1
        return number

    def getFirst(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if data[mid] == k:
            if mid < end and data[mid-1] == k:
                end = mid - 1
            else:
                return mid
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.getFirst(data, k, start, end)

    def getLast(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if data[mid] == k:
            if mid < end and data[mid+1] == k:
                start = mid + 1
            else:
                return mid
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        return self.getLast(data, k, start, end)

