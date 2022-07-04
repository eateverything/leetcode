# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.res = []

    # leetcode 22 括号生成
    def generateParenthesis(self, n: int) -> list[str]:
        self.backtrack(n, n, '')
        return self.res

    # left记录左括号剩余数量，right记录右括号剩余数量
    def backtrack(self, left, right, track):
        # 结束条件
        if right < left:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            self.res.append(track[:])
            return

        # 选择左括号
        track += '('
        self.backtrack(left - 1, right, track)
        track = track[: -1]

        # 选择右括号
        track += ')'
        self.backtrack(left, right - 1, track)
        track = track[0: -1]
