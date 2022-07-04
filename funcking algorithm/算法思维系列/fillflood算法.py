# -*- coding: utf-8 -*-

class Solution:
    # leetcode颜色填充
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        def fill(visited, image, sr, sc):
            visited[sr][sc] = 1
            image[sr][sc] = newColor
            direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for x, y in direct:
                newx = sr + x
                newy = sc + y
                if 0 <= newx < m and  0 <= newy < n and visited[newx][newy] == 0 and image[newx][newy] == origColor:
                    visited[newx][newy] = 1
                    image[newx][newy] = newColor
                    fill(visited, image, newx, newy)

        m = len(image)
        n = len(image[0])
        origColor = image[sr][sc]
        visited = [[0] * n for _ in range(m)]
        fill(visited, image, sr, sc)
        return image

    def floodFill2(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        def fill2(image, x, y, origColor, newColor):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return
            if image[x][y] != origColor:
                return
            if image[x][y] == -1:
                return
            image[x][y] = -1
            fill2(image, x, y + 1, origColor, newColor)
            fill2(image, x, y - 1, origColor, newColor)
            fill2(image, x - 1, y, origColor, newColor)
            fill2(image, x + 1, y, origColor, newColor)
            image[x][y] = newColor

        origColor = image[sr][sc]
        fill2(image, sr, sc, origColor, newColor)
        return image


    # leetcode 1034 边框着色
    def colorBorder(self, grid: list[list[int]], r0: int, c0: int, color: int) -> list[list[int]]:
        def fill(image, visited, x, y, origColor, newColor):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return 0
            if visited[x][y] == 1:
                return 1
            if image[x][y] != origColor:
                return 0
            visited[x][y] = 1
            surround = fill(image, visited, x, y+1, origColor, newColor) + \
                       fill(image, visited, x, y-1, origColor, newColor) + \
                       fill(image, visited, x+1, y, origColor, newColor) + \
                       fill(image, visited, x-1, y, origColor, newColor)
            if surround < 4:
                image[x][y] = newColor
            return 1

        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        origColor = grid[r0][c0]
        fill(grid, visited, r0, c0, origColor, color)
        return grid

    # leetcode 130 被围绕的区域
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs1(board, visited, sr, sc):
            visited[sr][sc] = True
            direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for x, y in direct:
                newx = sr + x
                newy = sc + y
                if 0 <= newx < m and 0 <= newy < n and visited[newx][newy] is False and board[newx][newy] == 'O':
                    dfs1(board, visited, newx, newy)
            return

        def dfs2(board, visited, sr, sc):
            visited[sr][sc] = True
            board[sr][sc] = 'X'
            direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for x, y in direct:
                newx = sr + x
                newy = sc + y
                if 0 <= newx < m and 0 <= newy < n and visited[newx][newy] is False and board[newx][newy] == 'O':
                    dfs2(board, visited, newx, newy)
            return

        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(n):
            if board[0][i] == 'O':
                dfs1(board, visited, 0, i)
        for i in range(m):
            if board[i][0] == 'O':
                dfs1(board, visited, i, 0)
        for i in range(n):
            if board[m-1][i] == 'O':
                dfs1(board, visited, m-1, i)
        for i in range(m):
            if board[i][n-1] == 'O':
                dfs1(board, visited, i, n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    dfs2(board, visited, i, j)



