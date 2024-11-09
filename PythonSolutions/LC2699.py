from collections import defaultdict
from heapq import *


class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        neg = set()
        e = defaultdict(list)
        for i in range(len(edges)):
            u, v, dist = edges[i]
            if dist == -1:
                neg.add(i)
            else:
                e[u].append(i)
                e[v].append(i)

        def dijkstra(graph):
            costs = [float("inf")] * n
            costs[source] = 0
            visited = [0] * n
            q = [(0, source)]
            while q:
                currentCost, currentNode = heappop(q)
                if not visited[currentNode]:
                    adjEdges = graph[currentNode]
                    for edge in adjEdges:
                        u, v, cost = edges[edge]
                        dest = u if v == currentNode else v
                        newCost = currentCost + cost
                        if newCost < costs[dest]:
                            costs[dest] = newCost
                            heappush(q, (newCost, dest))
                    visited[currentNode] = 1
            return costs[destination]

        # first pass without negative edges
        firstPass = dijkstra(e)

        if firstPass < target and firstPass != float("inf"):
            return []

        if firstPass == target:
            for i in neg:
                edges[i][2] = target
            return edges

        # modify edges
        for edgeIndex in neg:
            u, v, cost = edges[edgeIndex]
            edges[edgeIndex][2] = 1
            e[u].append(edgeIndex)
            e[v].append(edgeIndex)
            nextPass = dijkstra(e)
            if nextPass <= target:
                edges[edgeIndex][2] += target - nextPass
                for i in neg:
                    if edges[i][2] == -1:
                        edges[i][2] = target
                return edges
        return []
