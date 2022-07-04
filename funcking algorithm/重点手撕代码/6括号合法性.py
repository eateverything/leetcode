# -*- coding: utf-8 -*-

class Solution:
    # leetcode 20 有效的括号
    def isValid(self, s: str) -> bool:
        def leftOf(c):
            if c == ')':
                return '('
            elif c == ']':
                return '['
            else:
                return '{'

        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == leftOf(c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    # leetcode 22 括号生成
    def generateParenthesis(self, n: int) -> list[str]:
        # left记录左括号剩余个数，right记录右括号剩余个数
        def backtrace(left, right, trace):
            # 回溯，递归要先考虑终止条件
            if left < 0 or right < 0:
                return
            if left > right:
                return
            if left == 0 and right == 0:
                res.append(trace[:])
                return

            # 选择左括号
            trace += '('
            backtrace(left - 1, right, trace)
            trace = trace[: -1]

            # 选择右括号
            trace += ')'
            backtrace(left, right - 1, trace)
            trace = trace[: -1]

        res = []
        trace = ''
        backtrace(n, n, trace)
        return res

    # leetcode 921 使括号有效的最少添加
    def minAddToMakeValid(self, S: str) -> int:
        if len(S) <= 0:
            return 0

        res = 0
        # 右括号的需求量
        need = 0

        for c in S:
            if c == '(':
                need += 1
            else:
                need -= 1
                if need < 0:
                    res += 1
                    need = 0
        return res + need

    # leetcode 1541 平衡括号字符串的最小插入次数，即一个 ( 对应两个 ））
    def minInsertions(self, s: str) -> int:
        if len(s) <= 0:
            return 0

        res = 0
        # 右括号的需求量
        need = 0

        for c in s:
            if c == '(':
                need += 2
                # 如果need是奇数，需求1个就可以了
                if need % 2 == 1:
                    res += 1
                    need -= 1
            else:
                need -= 1
                if need < 0:
                    res += 1
                    need = 1
        return res + need

