# -*- coding: utf-8 -*-


class Sort_algorithm(object):
    def merge_sort(self, nums):
        def merge(a, b):
            c = []
            i, j = 0, 0
            while i<len(a) and j<len(b):
                if a[i] < b[j]:
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1
            while i<len(a):
                c.append(a[i])
                i += 1
            while j<len(b):
                c.append(b[j])
                j += 1
            return c

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return merge(left, right)

    def quick_sort(self, nums):
        def sort(nums, left, right):
            if left > right:
                return
            tmp = nums[left]
            i = left
            j = right
            while i <= j:
                while i <= j and nums[i] <= tmp:
                    i += 1
                while i <= j and nums[j] >= tmp:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[left], nums[j] = nums[j], nums[left]

            sort(nums, left, j-1)
            sort(nums, j+1, right)

        sort(nums, 0, len(nums)-1)
        return nums

    # 数组中的逆序对数
    def inversePairs(self, data):
        def inversePairsCore(data, copy, start, end):
            if start >= end:
                copy[start] = data[start]
                return 0
            length = (end - start) // 2
            left = inversePairsCore(copy, data, start, start+length)
            right = inversePairsCore(copy, data, start+length+1, end)
            count = 0
            i = start+length
            j = end
            index = end
            while i >= start and j >= start+length+1:
                if data[i] <= data[j]:
                    copy[index] = data[j]
                    j -= 1
                    index -= 1
                else:
                    copy[index] = data[i]
                    i -= 1
                    index -= 1
                    count += j - start - length
            while i >= start:
                copy[index] = data[i]
                i -= 1
                index -= 1
            while j >= start+length+1:
                copy[index] = data[j]
                j -= 1
                index -= 1
            return left+right+count

        length = len(data)
        if data is None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        result = inversePairsCore(data, copy, 0, length-1)
        return result



if __name__ == "__main__":
    nums = [1, 3, 2, 5, 3, 6, 7, 2, 199, 32, 6, 3, 7]
    sort_method = Sort_algorithm()
    merge_sort_nums = sort_method.merge_sort(nums)
    quick_sort_nums = sort_method.quick_sort(nums)
    print(merge_sort_nums)
    print(quick_sort_nums)
    print(sort_method.inversePairs([2, 1, 5, 4, 4]))