# -*- coding -*-

class Solution:
    # leetcode 969 煎饼排序
    def __init__(self):
        self.res = []

    def pancakeSort(self, A: list[int]) -> list[int]:
        self.sort(A, len(A))
        return self.res

    def sort(self, cakes, n):
        if n == 1:
            return
        maxCake = 0
        maxCakeIndex = 0
        for i in range(0, n):
            if cakes[i] > maxCake:
                maxCake = cakes[i]
                maxCakeIndex = i

        # 第一次反转，把最大的饼翻到最上边
        self.reverse(cakes, 0, maxCakeIndex)
        self.res.append(maxCakeIndex+1)
        # 第二次反转，把最大的蛋糕翻转到最下边
        self.reverse(cakes, 0, n-1)
        self.res.append(n)
        self.sort(cakes, 0, n-1)

    def reverse(self, cakes, i, j):
        while i < j:
            cakes[i], cakes[j] = cakes[j], cakes[i]
            i += 1
            j -= 1
