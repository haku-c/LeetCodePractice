from collections import deque


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]
        queue = deque([(0, 0, 0)])
        directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            cost, currentX, currentY = queue.popleft()
            if currentX == m - 1 and currentY == n - 1:
                return cost
            direction = grid[currentX][currentY]
            for i in range(1, 5):
                newX = currentX + directions[i][0]
                newY = currentY + directions[i][1]
                newCost = cost if direction == i else cost + 1
                if 0 <= newX < m and 0 <= newY < n and (newCost < dist[newX][newY]):
                    dist[newX][newY] = newCost
                    if direction == i:
                        queue.appendleft((cost, newX, newY))
                    else:
                        queue.append((cost + 1, newX, newY))
        return -1


# use Dijkstra's: don't visit all elements with a visited, instead only add if going results in a lower cost (track found distances)
# also, we can use a deque since we either add to the end or add to the front for each queue append.
# this is instead of a heap, which we would need if a new append would need to go somewhere in the middle of the queue
