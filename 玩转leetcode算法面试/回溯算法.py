# -*- coding:utf-8 -*-

class Solution:
    # 131分割回文串
    def partition(self, s: str) -> list[list[str]]:
        def isPalindrome(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def helper(s, pos):
            if pos == len(s):
                res.append(path[:])
                return
            for i in range(pos, len(s)):
                if isPalindrome(s[pos:i+1]):
                    path.append(s[pos:i+1])
                    helper(s, i+1)
                    path.pop()

        res, path = [], []
        helper(s, 0)
        return res

    # 46全排列
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, path = [], []
        used = [False] * len(nums)

        def backtrack(nums, index):
            if index == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] is False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, index+1)
                    used[i] = False
                    path.pop()

        backtrack(nums, 0)
        return res

    # 47全排列II
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res, path = [], []
        used = [False] * len(nums)

        def backtrack(nums, index):
            if index == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] is False:
                    continue
                if used[i] is False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, index + 1)
                    used[i] = False
                    path.pop()
        nums.sort()
        backtrack(nums, 0)
        return res

    # 77组合
    def combine(self, n: int, k: int) -> list[list[int]]:
        res, path = [], []

        def backtrack(n, k, index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(index, n + 1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res

    # 39组合总和
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, path = [], []

        def backtrack(nums, target, sum, index):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return
            for i in range(index, len(nums)):
                sum += nums[i]
                path.append(nums[i])
                backtrack(nums, target, sum, i)
                path.pop()
                sum -= nums[i]

        backtrack(candidates, target, 0, 0)
        return res

    # 40组合总和II
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res, path = [], []
        used = [False] * len(candidates)

        def backtrack(nums, target, sum, index):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return
            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] is False:
                    continue
                if used[i] is False:
                    sum += nums[i]
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, target, sum, i+1)
                    used[i] = False
                    path.pop()
                    sum -= nums[i]

        candidates.sort()
        backtrack(candidates, target, 0, 0)
        return res

    # 216组合总和III
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res, path = [], []
        used = [False] * 10

        def backtrack(num, k, n, index):
            if len(path) == k and n == 0:
                res.append(path[:])
                return

            for i in range(index, num):
                if used[i] is False:
                    path.append(i)
                    backtrack(num, k, n-i, i+1)
                    path.pop()

        backtrack(10, k, n, 1)
        return res

    # 78子集
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, path = [], []
        used = [False] * len(nums)

        def backtrack(nums, index):
            if len(path) > len(nums):
                return
            res.append(path[:])
            for i in range(index, len(nums)):
                if used[i] is False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, i+1)
                    used[i] = False
                    path.pop()

        backtrack(nums, 0)
        return res

    # 90子集II
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res, path = [], []
        used = [False] * len(nums)

        def backtrack(nums, index):
            if len(path) > len(nums):
                return
            res.append(path[:])
            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] is False:
                    continue
                if used[i] is False:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, i + 1)
                    used[i] = False
                    path.pop()

        nums.sort()
        backtrack(nums, 0)
        return res

    # 79单次搜索
    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = [[False] * n for _ in range(m)]

        def inArea(x, y):
            return x >= 0 and y >= 0 and x < m and y < n

        def searchWord(board, startx, starty, word, index):
            if index == len(word) - 1:
                return board[startx][starty] == word[index]
            if board[startx][starty] == word[index]:
                visit[startx][starty] = True
                for i in range(4):
                    newx = startx + d[i][0]
                    newy = starty + d[i][1]
                    if inArea(newx, newy) and visit[newx][newy] is False:
                        if searchWord(board, newx, newy, word, index+1):
                            return True
                visit[startx][starty] = False
            return False

        for i in range(m):
            for j in range(n):
                if searchWord(board, i, j, word, 0):
                    return True
        return False

    # 200岛屿数量
    def numIslands(self, grid: list[list[str]]) -> int:
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = [[False] * n for _ in range(m)]

        def inArea(x, y):
            return x >= 0 and y >= 0 and x < m and y < n

        def dfs(grid, x, y):
            visit[x][y] = True
            for i in range(4):
                newx = x + d[i][0]
                newy = y + d[i][1]
                if inArea(newx, newy) and grid[newx][newy] == '1' and visit[newx][newy] == False:
                    dfs(grid, newx, newy)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visit[i][j] == False:
                    res += 1
                    dfs(grid, i, j)
        return res


