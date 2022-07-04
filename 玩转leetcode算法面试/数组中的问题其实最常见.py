# -*- coding: utf-8 -*-


class Solution:
    # 283 move zero
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        return nums

    # 27移除元素
    def removeElement(self, nums: list[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

    # 26删除有序数组中的重复项
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1

    # 80删除有序数组中的重复项II
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        pre = nums[0]
        sum = 1
        cnt = 1
        for i in range(1, n):
            if nums[i] == pre:
                cnt += 1
                if cnt <= 2:
                    nums[sum] = nums[i]
                    sum += 1
            else:
                nums[sum] = nums[i]
                cnt = 1
                sum += 1
                pre = nums[i]
        return sum

    # 75颜色分类
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = -1
        two = n
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1

    # 215数组中的第k个最大元素
    def findKthLargest(self, nums: list[int], k: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            i = lo
            j = hi - 1
            temp = nums[lo]
            while i <= j:
                while i <= j and nums[i] >= temp:
                    i += 1
                while i <= j and nums[j] < temp:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[j], nums[lo] = nums[lo], nums[j]
            if j == k-1:
                return nums[j]
            elif j < k-1:
                lo = j + 1
            else:
                hi = j

    # 167 两数之和-输入有序数组
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 对撞指针
        slow = 0
        fast = len(numbers) - 1
        while slow < fast:
            if numbers[slow] + numbers[fast] == target:
                return [slow+1, fast+1]
            elif numbers[slow] + numbers[fast] > target:
                fast -= 1
            else:
                slow += 1
        return []

    # 11乘最多水的容器
    def maxArea(self, height: list[int]) -> int:
        # 对撞指针
        i, j, h, max_area = 0, len(height)-1, 0, 0
        while i <= j:
            h = min(height[i], height[j])
            max_area = max(max_area, h*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

    # 滑动窗口
    # 209长度最小的子数组
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        r = -1
        res = len(nums) + 1
        sum = 0
        while l < len(nums):
            if sum < target and r+1 < len(nums):
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            if sum >= target:
                res = min(res, r-l+1)
        return res

    # 3无重复字符的最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        need = {}
        while r < len(s):
            c = s[r]
            r += 1
            need[c] = need.get(c, 0) + 1
            while need[c] > 1:
                d = s[l]
                l += 1
                need[d] -= 1
            max_len = max(max_len, r-l)
        return max_len

    # 76最小覆盖子串
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        l, r = 0, 0
        min_len = len(s) + 1
        start = 0
        valid = 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if r-l < min_len:
                    start = l
                    min_len = r-l
                d = s[l]
                l += 1
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid -= 1
        return '' if min_len == len(s)+1 else s[start: start+min_len]

    # 33搜索旋转排序数组
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # 45跳跃游戏II
    def jump1(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        jump = 0
        end = 0
        farest = 0
        for i in range(n-1):
            farest = max(farest, i+nums[i])
            if end == i:
                jump += 1
                end = farest
        return jump

    def jump2(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        range = 1
        jump = 0
        i = 1
        next = 0
        while range < n:
            if i <= range:
                next = max(next, i+nums[i-1])
                i += 1
            else:
                jump += 1
                range = next
        return jump

    # 42 接雨水
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        lh = 0
        rh = n - 1
        res = 0
        lmax = height[lh]
        rmax = height[rh]
        while lh < rh:
            lmax = max(lmax, height[lh])
            rmax = max(rmax, height[rh])
            if lmax < rmax:
                res += lmax - height[lh]
                lh += 1
            else:
                res += rmax - height[rh]
                rh -= 1
        return res

    # 41缺失的第一个正数
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


