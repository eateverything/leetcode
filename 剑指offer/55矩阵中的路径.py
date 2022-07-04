# -*- coding:utf-8 -*-

'''
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个
格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路
径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含
"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix and rows <= 0 and cols <= 0 and path is None:
            return False
        markMatrix = [False] * (rows * cols)
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, row, col, rows, cols, path, pathLength, markMatrix):
                    return True
        return False

    def hasPathCore(self, matrix, row, col, rows, cols, path, pathLength, markMatrix):
        if pathLength == len(path):
            return True

        hasPath = False
        if row >= 0 and row < rows and col >=0 and col < cols and matrix[row*cols+col]==path[pathLength] and not markMatrix[row*cols+col]:
            pathLength += 1
            markMatrix[row*cols+col] = True
            hasPath = self.hasPathCore(matrix, row + 1, col, rows, cols, path, pathLength, markMatrix) \
                    or self.hasPathCore(matrix, row - 1, col, rows, cols, path, pathLength, markMatrix) \
                    or self.hasPathCore(matrix, row , col + 1, rows, cols, path, pathLength, markMatrix) \
                    or self.hasPathCore(matrix, row, col - 1, rows, cols, path, pathLength, markMatrix)

            if not hasPath:
                pathLength -= 1
                markMatrix[row*cols+col] = False
        return hasPath