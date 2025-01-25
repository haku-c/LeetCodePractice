from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m = len(isWater)
        n = len(isWater[0])
        visited = [[0] * n for _ in range(m)]
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((0, i, j))
        while queue:
            height, row, col = queue.popleft()
            for deltaRow, deltaCol in directions:
                newRow, newCol = row + deltaRow, col + deltaCol
                if (
                    0 <= newRow < m
                    and 0 <= newCol < n
                    and not (visited[newRow][newCol] > 0)
                    and not isWater[newRow][newCol]
                ):
                    visited[newRow][newCol] = height + 1
                    queue.append((height + 1, newRow, newCol))
        return visited


# note how you can use a deque here because you traverse in minimum order you will never need to add a new square into the middle of the queue
# so you can use the deque for the fast O(1) appends (instead of a hashmap)
# guaranteed to add something to the end of the queue when exploring in the bfs

# always want to explore from the cell with lowest heights
# start with all the water cells since they must be 0
# don't forget you can't override water cells
