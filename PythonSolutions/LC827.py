from collections import deque
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
    def find(self,x):
        if self.parents[x] == x:
            return x
        return self.find(self.parents[x])
    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)
        if repx == repy:
            return

        sizex = self.sizes[repx]
        sizey = self.sizes[repy]
        if sizex > sizey:
            self.parents[repy] = repx
            self.sizes[repx] += sizey
        else:
            self.parents[repx] = repy
            self.sizes[repy] += sizex

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = [[0] * n for _ in range(n)]
        uf = UnionFind(n * n)
        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                index = row * n + col
                for deltaRow, deltaCol in directions:
                    newRow, newCol = row + deltaRow, col + deltaCol
                    if 0 <= newRow < n and 0 <= newCol < n and not visited[newRow][newCol] and grid[newRow][newCol]:
                        visited[newRow][newCol] = 1
                        uf.union(index, newRow * n + newCol)
                        queue.append((newRow, newCol))
        # track all connected components and their sizes
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    bfs(i,j)
        # apply the operation to one island -> connects the adjacent components
        # print(uf.parents)
        # print(uf.sizes)
        res = max(uf.sizes)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    current = 1
                    adj = set()
                    # check the four adjacent cells to see if they are part of an island
                    for deltaRow, deltaCol in directions:
                        newRow, newCol = i + deltaRow, j + deltaCol
                        if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 1:
                            # check if adjacent cells are in different components, add unique components
                            index = newRow * n + newCol 
                            rep = uf.find(index)
                            adj.add(rep)
                    for reps in adj:
                        current += uf.sizes[reps]
                    res = max(res, current)
        return res 