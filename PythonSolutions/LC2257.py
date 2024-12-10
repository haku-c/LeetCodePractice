class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for row, col in guards:
            grid[row][col] = 1
        for row, col in walls:
            grid[row][col] = 1
        for row, col in guards:
            # North
            i = row - 1
            while i >= 0 and grid[i][col] != 1:
                grid[i][col] = 2
                i -= 1
            # East
            i = col + 1
            while i < n and grid[row][i] != 1:
                grid[row][i] = 2
                i += 1
            # South
            i = row + 1
            while i < m and grid[i][col] != 1:
                grid[i][col] = 2
                i += 1
            # West
            i = col - 1
            while i >= 0 and grid[row][i] != 1:
                grid[row][i] = 2
                i -= 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count


# you want to use a while loop for each direction because we stop once we hit the wall or once we hit a guard
