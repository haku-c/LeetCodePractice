class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        self.size = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def recurse(row, col):
            if visited[row][col] or not grid[row][col]:
                return
            visited[row][col] = 1
            self.size += 1
            for x, y in directions:
                if row + x >= 0 and row + x < m and col + y >= 0 and col + y < n:
                    recurse(row + x, col + y)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    recurse(i, j)
                    res = max(res, self.size)
                    self.size = 0
        return res


# dfs. track visited coordinates to minimize repeats. Track a global size
# use the directions array for better traversal logic.
