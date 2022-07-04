# -*- coding: utf-8 -*-


class Solution:
    # leetcode 33 搜索排序旋转数组
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 总会有一侧是保持升序的，好判断
            # 左侧有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            # 右侧有序
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # leetcode 81 搜索排序旋转数组II
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue
            # 总会有一侧是保持升序的，好判断
            # 左侧有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右侧有序
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

    # 数组中的逆序对
    def reversePairs(self, nums: list[int]) -> int:
        def reversePairsCore(data, copy, start, end):
            # 递归终止条件
            if start == end:
                copy[start] = data[start]
                return 0

            length = (end - start) // 2

            # 此处data和copy每次交换的目的是用于比较的数组要是排好序的
            left = reversePairsCore(copy, data, start, start+length)
            right = reversePairsCore(copy, data, start+length+1, end)

            i = start+length
            j = end
            index = end
            count = 0
            while i >= start and j >= start+length+1:
                if data[i] > data[j]:
                    copy[index] = data[i]
                    index -= 1
                    i -= 1
                    count += j - start - length
                else:
                    copy[index] = data[j]
                    j -= 1
                    index -= 1

            while i >= start:
                copy[index] = data[i]
                index -= 1
                i -= 1
            while j >= start+length+1:
                copy[index] = data[j]
                j -= 1
                index -= 1

            return left + right + count

        length = len(nums)
        if nums is None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = nums[i]

        return reversePairsCore(nums, copy, 0, length-1)




