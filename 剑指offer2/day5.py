# -*- coding: utf-8 -*-

'''
5. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = 1
        number = numbers[0]
        for num in numbers[1:]:
            if num == number:
                count += 1
            else:
                count -= 1
            if count == 0:
                number = num
                count += 1
        sum = 0
        for j in numbers:
            if j == number:
                sum += 1
        return number if sum > len(numbers) // 2 else 0


'''
2. 最小的k个数
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
# 堆排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) <= 0 or k <= 0 or len(tinput) < k:
            return []
        self.minHeap(tinput)
        result = []
        count = 0
        while count < k:
            result.append(tinput.pop(0))
            count += 1
            self.minHeap(tinput)
        return result

    def minHeap(self, alist):
        length = len(alist)
        if alist is None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length//2, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length -1:
                    if alist[index+1] < alist[index]:
                        index += 1
                if temp < alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp


'''
3.连续子数组的最大和
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        curMax = sumMax = array[0]
        for i in range(1, len(array)):
            curMax = max(array[i], curMax+array[i])
            sumMax = max(curMax, sumMax)
        return sumMax


'''
4.把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
'''
# 这道题其实希望我们能够找到一个排序规则，数组根据这个规则排序之后能排成一个最小的数字。要确定排序的规则，就要比较两个数字，
# 也就是给出两个数字m和n，我们需要确定一个规则判断m和n哪个应该排在前面，而不是仅仅比较这两个数字的值哪个更大。
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers is None:
            return ""
        arr = [str(x) for x in numbers]
        arr.sort(lambda x, y: cmp(x+y, y+x))
        return "".join(arr)


 '''
 5.丑数
 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
 '''
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        res = [1]
        index2 = index3 = index5 = 0
        nextindex = 1
        while nextindex < index:
            minNum = min(res[index2] * 2, res[index3] * 3, res[index5] * 5)
            res.append(minNum)

            while res[index2] * 2 <= minNum:
                index2 += 1

            while res[index3] * 3 <= minNum:
                index3 += 1

            while res[index5] * 5 <= minNum:
                index5 += 1

            nextindex += 1
        return res[index-1]


'''
6.数组中的逆序对数
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007
'''
# 递归会超时呀
class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) > 1:
            mid = len(data) // 2
            left_data = data[:mid]
            right_data = data[mid:]
            left_count = self.InversePairs(left_data) % 1000000007
            right_count = self.InversePairs(right_data) % 1000000007
            i, j, k, count = len(left_data) - 1, len(right_data) - 1, len(data) - 1, 0
            while i >= 0 and j >= 0:
                if left_data[i] < right_data[j]:
                    data[k] = right_data[j]
                    k -= 1
                    j -= 1
                else:
                    count += (j + 1)
                    data[k] = left_data[i]
                    i -= 1
                    k -= 1
            while i >= 0:
                data[k] = left_data[i]
                k -= 1
                i -= 1
            while j >= 0:
                data[k] = right_data[j]
                k -= 1
                j -= 1
            return (count + left_count + right_count) % 1000000007
        else:
            return 0




