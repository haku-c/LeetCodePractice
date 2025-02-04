from collections import deque


class Solution:
    # standard bfs solution, does reset grid to all 0s for easier logic

    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        m = len(grid)
        n = len(grid[0])
        self.res = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            currentFish = 0
            while queue:
                row, col = queue.popleft()
                currentFish += grid[row][col]
                self.res = max(self.res, currentFish)
                grid[row][col] = 0
                for deltaRow, deltaCol in directions:
                    newRow, newCol = row + deltaRow, col + deltaCol
                    if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] > 0:
                        queue.append((newRow, newCol))

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    bfs(i, j)
        return self.res


# standard dfs solution, don't forget to return 0 if the cell is already explored or empty
def findMaxFish2(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    self.res = 0

    def dfs(row, col):
        if 0 <= row < m and 0 <= col < n and grid[row][col] > 0:
            val = grid[row][col]
            grid[row][col] = 0
            return (
                val
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col - 1)
                + dfs(row, col + 1)
            )
        return 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                self.res = max(self.res, dfs(i, j))

    return self.res
