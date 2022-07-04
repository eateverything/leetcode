# -*- coding: utf-8 -*-

class UF():
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.size = []

        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return

        if self.size[p] > self.size[q]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.count -= 1

    def connect(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return True
        return False


class Solution:
    # leetcode 990 等式方程的可满足性
    def equationsPossible(self, equations: list[str]) -> bool:
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        parent = [0] * 26
        for i in range(26):
            parent[i] = i

        for eq in equations:
            x = eq[0]
            y = eq[3]
            if eq[1] == '=':
                rootx = find(ord(x) - ord('a'))
                rooty = find(ord(y) - ord('a'))
                if rootx != rooty:
                    parent[rooty] = rootx

        for eq in equations:
            x = eq[0]
            y = eq[3]
            if eq[1] == '!':
                rootx = find(ord(x) - ord('a'))
                rooty = find(ord(y) - ord('a'))
                if rootx == rooty:
                    return False
        return True