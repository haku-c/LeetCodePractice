class Solution:
    # O(m) memory, O(mn) time
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pastCol = [0] * m
        res = 0
        # track the max number of moves that can be achieved by ending on the current square.
        for j in range(1, n):
            currentCol = []
            for i in range(m):
                temp = [0]
                if (i + 1) < m and grid[i + 1][j - 1] < grid[i][j]:
                    temp.append(pastCol[i + 1] + 1)
                if (i - 1) >= 0 and grid[i - 1][j - 1] < grid[i][j]:
                    temp.append(pastCol[i - 1] + 1)
                if grid[i][j - 1] < grid[i][j]:
                    temp.append(pastCol[i] + 1)
                currentCol.append(max(temp))
            pastCol = currentCol
            # early termination if we cannot keep moving because all the values in the left column were greater
            if max(pastCol) == res:
                return res
            else:
                res = max(res, max(pastCol))
        return res
