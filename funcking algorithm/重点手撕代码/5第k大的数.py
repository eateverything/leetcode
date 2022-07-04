# -*- coding: utf-8 -*-

from heapq import *
# leetcode 703数据流中的第K大元素
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minh = []
        self.k = k
        heapify(self.minh)
        for num in nums:
            heappush(self.minh, num)
            if len(self.minh) > self.k:
                heappop(self.minh)

    def add(self, val: int) -> int:
        heappush(self.minh, val)
        if len(self.minh) > self.k:
            heappop(self.minh)
        return self.minh[0]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # leetcode 230 二叉搜索树中第k小的元素
    # 二叉搜索树的中序遍历就是一个有序数组
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        sort_nums = []
        def sortNums(root):
            # 递归一定要记得写终止条件
            if root is None:
                return
            sortNums(root.left)
            sort_nums.append(root.val)
            sortNums(root.right)

        sortNums(root)
        return sort_nums[k - 1]

    # leetcode 215 数组中的第k个最大元素
    # 快排的变种
    def findKthLargest(self, nums: list[int], k: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            i = low
            j = high - 1
            tmp = nums[low]
            # 快排思想：比tmp大的都放在前边，小的都放在后边
            while i <= j:
                while i <= j and nums[i] >= tmp:
                    i += 1
                while i <= j and nums[j] < tmp:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[low], nums[j] = nums[j], nums[low]

            if j == k - 1:
                return nums[j]
            elif j < k - 1:
                low = j + 1
            else:
                high = j

    # leetcode 378 有序矩阵第k小的元素
    # 大顶堆,python只有小顶堆，没有大顶堆
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        maxh = []
        heapify(maxh)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(maxh, -matrix[i][j])
                if len(maxh) > k:
                    heappop(maxh)
        return -maxh[0]