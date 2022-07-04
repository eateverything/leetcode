# -*- coding: utf-8 -*-


class Solution:
    # leetcode 20 有效的括号
    # 用栈来解决
    def isValid(self, s: str) -> bool:
        def leftOf(c):
            if c == ')':
                return '('
            elif c == ']':
                return '['
            return '{'

        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) > 0 and leftOf(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

