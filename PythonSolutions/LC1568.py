# this solution uses Tarjan's algorithm. If there is an articulation point to disconnect a strongly connected component
# return 1
# if 2 ccs, return 0
# otherwise return 2
# also edge cases with only 1 instance of land
# lc also accepts the brute force solution where you change each instance of land to water and test if there are more than one ccs


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        self.hasArticulation = False
        s = 0
        for row in grid:
            for i in row:
                s += i
        if s == 1:
            return 1
        elif s == 0:
            return 0
        # if you can find an articulation point, return 1
        # otherwise, return 2
        m = len(grid)
        n = len(grid[0])
        # traverse using the row and column numbers as the node id's
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[0] * n for i in range(m)]
        disc = [[0] * n for i in range(m)]
        low = [[0] * n for i in range(m)]
        parents = [[(-1, -1) for j in range(n)] for i in range(m)]
        self.order = 1

        def traverse(row, col):
            children = 0
            disc[row][col] = self.order
            visited[row][col] = 1
            low[row][col] = self.order
            self.order += 1
            res = False
            for d in directions:
                x, y = d
                newRow = row + x
                newCol = col + y
                if (
                    newRow >= 0
                    and newRow < m
                    and newCol >= 0
                    and newCol < n
                    and grid[newRow][newCol]
                ):
                    if not visited[newRow][newCol]:
                        parents[newRow][newCol] = (row, col)
                        children += 1
                        res = traverse(newRow, newCol)
                        low[row][col] = min(low[row][col], low[newRow][newCol])
                        if parents[row][col] == (-1, -1) and children > 1:
                            self.hasArticulation = True
                        if (
                            parents[row][col] != (-1, -1)
                            and low[newRow][newCol] >= disc[row][col]
                        ):
                            self.hasArticulation = True
                    elif (newRow, newCol) != parents[row][col]:
                        low[row][col] = min(low[row][col], disc[newRow][newCol])

        one = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not one and not visited[i][j]:
                    traverse(i, j)
                    one = True
                elif grid[i][j] == 1 and not visited[i][j]:
                    return 0
        if self.hasArticulation:
            return 1

        return 2
