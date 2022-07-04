# -*- coding -*-

class Solution:
    # leetcode 167 两数之和II
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        return []

    # leetcode 1 两数之和, 如果是返回具体值，那就更简单了
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i, num in enumerate(nums):
            index[num] = i

        for i in range(len(nums)):
            if (target - nums[i]) in index and index[target-nums[i]] != i:
                return [i, index[target-nums[i]]]
        return []


    # nSum问题通用模板
    def nSum(self, nums, n, start, target):
        sz = len(nums)
        res = []
        if n < 2 or sz < n:
            return res
        if n == 2:
            lo = start
            hi = sz - 1
            while lo < hi:
                sum = nums[lo] + nums[hi]
                left = nums[lo]
                right = nums[hi]
                if sum < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif sum > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            # for i in range(start, sz): 循环内的加1不影响for内i的递增
            i = start
            while i < sz:
                print(i)
                sub = self.nSum(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < sz - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return res


if __name__ == "__main__":
    so = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums.sort()
    res = so.nSum(nums, 3, 0, 0)
    print(res)