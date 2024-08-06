"""
grid: List[List[str]]
numIslands -> int
"""


class Solution(object):

    def numIslands(self, grid):
        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return

            # 방문한 곳
            grid[i][j] = 0

            # 연결된 1에 대해 dfs 수행
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt
