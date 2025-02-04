class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * (n)

    def find(self, i):
        if self.parents[i] == i:
            return i
        return self.find(self.parents[i])

    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)
        if repx == repy:
            return
        if self.size[repx] > self.size[repy]:
            self.size[repx] += self.size[repy]
            self.parents[repy] = repx
        else:
            self.parents[repx] = repy
            self.size[repy] += self.size[repx]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        for x, y in edges:
            if uf.find(x) == uf.find(y):
                return [x, y]
            else:
                uf.union(x, y)


# union find solution

from collections import defaultdict, deque


# i'm a bit partial to vanilla bfs/dfs though
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = [0] * n
        queue = deque([1])
        while queue:
            current = queue.popleft()
            visited[current] = 1
            for dest in graph[current]:
                if visited[dest]:
                    break
                else:
                    queue.append(dest)
        for i in range(n, -1, -1):
            x, y = edges[i]
            if visited[x] and visited[y]:
                return [x, y]
