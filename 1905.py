class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0] * n for i in range(m)]
        groups = [i for i in range(m * n)]
        sums = []

        def traverse(group, row, col):
            if visited[row][col]:
                return
            visited[row][col] = 1
            if grid1[row][col]:
                groups[row * n + col] = group
                for x, y in directions:
                    newRow, newCol = row + x, col + y
                    if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n:
                        traverse(group, newRow, newCol)

        # setup the data structure to identify
        for i in range(m):
            for j in range(n):
                if grid1[i][j] and not visited[i][j]:
                    traverse(i * n + j, i, j)

        visited = [[0] * n for i in range(m)]

        def traverse2(group, row, col):
            if visited[row][col]:
                return
            visited[row][col] = 1
            if grid2[row][col]:
                if groups[row * n + col] != group or not grid1[row][col]:
                    sums[-1] = 0
                for x, y in directions:
                    newRow, newCol = row + x, col + y
                    if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n:
                        traverse2(group, newRow, newCol)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] and not visited[i][j]:
                    sums.append(1)
                    traverse2(groups[i * n + j], i, j)

        return sum(sums)


# # union find impl
# class UnionSet:
#     def __init__(self, n):
#         self.parent = [i for i in range(n + 1)]
#         self.sizes = [1] * (n + 1)

#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]

#     def union(self, x, y):
#         xrep = self.find(x)
#         yrep = self.find(y)
#         xsize = self.sizes[xrep]
#         ysize = self.sizes[yrep]
#         if xrep == yrep:
#             return
#         if ysize > xsize:
#             self.parent[xrep] = yrep
#             self.sizes[yrep] += xsize
#         else:
#             self.parent[yrep] = xrep
#             self.sizes[xrep] += ysize


# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         m = len(grid1)
#         n = len(grid1[0])
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         visited = [[0] * n for i in range(m)]
#         us = UnionSet(m * n)
#         sums = []

#         def traverse(group, row, col):
#             if visited[row][col]:
#                 return
#             currentIndex = row * n + col
#             visited[row][col] = 1
#             if grid1[row][col]:
#                 us.union(group, currentIndex)
#                 for x, y in directions:
#                     newRow, newCol = row + x, col + y
#                     if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n:
#                         traverse(group, newRow, newCol)

#         # setup the data structure to identify
#         for i in range(m):
#             for j in range(n):
#                 if grid1[i][j] and not visited[i][j]:
#                     currentIndex = i * n + j
#                     traverse(currentIndex, i, j)

#         visited = [[0] * n for i in range(m)]

#         def traverse2(group, row, col):
#             if visited[row][col]:
#                 return
#             currentIndex = row * n + col
#             visited[row][col] = 1
#             if grid2[row][col]:
#                 if us.find(currentIndex) != group or not grid1[row][col]:
#                     sums[-1] = 0
#                 for x, y in directions:
#                     newRow, newCol = row + x, col + y
#                     if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n:
#                         traverse2(group, newRow, newCol)

#         for i in range(m):
#             for j in range(n):
#                 if grid2[i][j] and not visited[i][j]:
#                     sums.append(1)
#                     currentIndex = i * n + j
#                     currentGroup = us.find(currentIndex)
#                     traverse2(currentGroup, i, j)

#         return sum(sums)
