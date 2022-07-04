# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.res = []
    # leetcode 78 子集
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums, start, track):
        self.res.append(track[:]) # 此处track[:]是要注意的地方，Python与其他语言处理方式不同
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i+1, track)
            track.pop()

    # leetcode 90 子集2
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        used = [False] * len(nums)
        nums.sort()
        self.backtrack1(nums, 0, [], used)
        return self.res

    def backtrack1(self, nums, start, track, used):
        self.res.append(track[:])
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            if used[i] == False:
                track.append(nums[i])
                used[i] = True
                self.backtrack1(nums, i+1, track, used)
                used[i] = False
                track.pop()

    def backtrack1_new(self, nums, start, track, used):
        self.res.append(track)
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            if used[i] == False:
                used[i] = True
                self.backtrack1(nums, i + 1, track + [nums[i]], used)
                used[i] = False

    # leetcode 77 组合
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.backtrack2(n, k, 1, [])
        return self.res

    def backtrack2(self, n, k, start, track):
        if len(track) == k:
            self.res.append(track[:])
            return

        for i in range(start, n+1):
            track.append(i)
            self.backtrack2(n, k, i+1, track)
            track.pop()

    # leetcode 46 全排列
    def permute(self, nums: list[int]) -> list[list[int]]:
        used = [False] * len(nums)
        self.backtrack3(nums, [], used)
        return self.res

    def backtrack3(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for i in range(0, len(nums)):
            if used[i] == True:
                continue
            track.append(nums[i])
            used[i] = True
            self.backtrack3(nums, track, used)
            used[i] = False
            track.pop()




