# -*- coding: utf-8 -*-

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backstrack(board, 0, 0)

    def backstrack(self, board, i, j):
        if j == 9:
            # 到头了，换下一行
            return self.backstrack(board, i+1, 0)
        if i == 9:
            # 找到答案了
            return True
        if board[i][j] != '.':
            return self.backstrack(board, i, j+1)
        for s in ('123456789'):
            # 遇到不合法的数字，就跳过
            if self.isValid(board, i, j, s) == False:
                continue

            board[i][j] = s
            # 找到一个可行解，立即结束
            if self.backstrack(board, i, j+1):
                return True
            board[i][j] = '.'
        return False

    def isValid(self, board, r, c, s):
        for i in range(0, 9):
            # 同一列有没有重复数字
            if board[r][i] == s:
                return False
            # 同一行有没有重复数字
            if board[i][c] == s:
                return False
            # 3*3的小方阵里有没有重复数字
            if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == s:
                return False
        return True