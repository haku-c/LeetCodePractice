import collections


# bfs solution. From an intuition standpoint, you can think of this as going layer by layer of what is reachable in a certain number of steps.
# you expand the "frontier" of squares reachable by 1 step, 2 steps, etc.
# example below: 0s are open spaces, xs are original obstacles


# 0 0 0 0    1 2 0 0     1 2 3 0     1 2 3 4    1 2 3 4
# 0 x x 0    2 x x 0     2 x x 0     2 x x 0    2 x x 5
# 0 0 x 0    0 0 x 0     3 3 x 0     3 3 x 0    3 3 x 5
# 0 0 0 0    0 0 0 0     0 0 0 0     4 4 4 0    4 4 4 5
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
            [-1, -1],
            [1, 1],
            [-1, 1],
            [1, -1],
        ]
        if grid[0][0] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        n = len(grid)
        while queue:
            x, y, pathLen = queue.popleft()
            print(str(x) + " " + str(y))
            if (x, y) == (n - 1, n - 1):
                return pathLen
            for direction in directions:
                delX, delY = direction
                newX = x + delX
                newY = y + delY
                if (
                    newX >= 0
                    and newX < n
                    and newY >= 0
                    and newY < n
                    and grid[newX][newY] == 0
                ):
                    queue.append((newX, newY, pathLen + 1))
                    grid[newX][newY] = 1

        return -1
