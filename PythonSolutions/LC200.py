from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m = len(grid)
        n = len(grid[0])

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = "0"
            while queue:
                currentRow, currentCol = queue.popleft()
                for deltaRow, deltaCol in directions:
                    newRow, newCol = currentRow + deltaRow, currentCol + deltaCol
                    if (
                        0 <= newRow < m
                        and 0 <= newCol < n
                        and (grid[newRow][newCol] == "1")
                    ):
                        grid[newRow][newCol] = "0"
                        queue.append((newRow, newCol))

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res


# straightforward bfs solution
