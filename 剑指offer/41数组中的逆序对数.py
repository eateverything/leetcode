# -*- coding:utf-8 -*-

'''
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组
中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''


# 思路：考察的是归并排序的应用
class Solution:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count % 1000000007

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0

        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start+length+1, end)

        i = start+length
        j = end

        count = 0
        indexCopy = end

        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            j -= 1
            indexCopy -= 1
        return left + right + count


if __name__ == "__main__":
    print(Solution().InversePairs([2, 1, 3, 4]))
