import heapq
import List
from collections import defaultdict


# note I transform the queue into a max heap
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(edges) + 1
        # avoid cycles by tracking visited nodes
        self.visited = [False] * n
        self.res = 0
        # generate graph
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            length = []
            self.visited[node] = True
            for dest in graph[node]:
                if not self.visited[dest]:
                    heapq.heappush(length, -(1 + dfs(dest)))
            res = 0
            # we want to return the longest path consisting of unvisited nodes connected to this one
            if length:
                top = -length[0]
            else:
                return 0
            count = 0
            while length and count < 2:
                res += -heapq.heappop(length)
                count += 1
            # we want to find the longest possible path which may pass through this node. so we take the sum of the top 2 longest paths
            # of the unvisited nodes connected to this one
            self.res = max(self.res, res)
            return top

        dfs(0)
        return self.res


# this question is similar to LC543. (and 1522) The idea is the same, but instead of being a binary tree with a root,
# we have an undirected graph and a node can have more than 2 "children"

# The diameter of a tree is the number of edges in the longest path in that tree.

# There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

# Return the diameter of the tree.

# alternatively you can run bfs twice,
# first time to find the farthest from the start node
# second time to find the farthest node from what you found in step one
# the result is the sum


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        # build the adjacency list representation of the graph
        graph = [set() for i in range(len(edges) + 1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            """
            return the farthest node from the 'start' node
              and the distance between them.
            """
            visited = [False] * len(graph)

            visited[start] = True
            queue = deque([start])
            distance = -1
            last_node = start
            while queue:
                next_queue = deque()
                while queue:
                    next_node = queue.popleft()
                    for neighbor in graph[next_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            next_queue.append(neighbor)
                            last_node = neighbor
                distance += 1
                queue = next_queue

            return last_node, distance

        # 1). find one of the farthest nodes
        farthest_node, distance_1 = bfs(0)
        # 2). find the other farthest node
        #  and the distance between two farthest nodes
        another_farthest_node, distance_2 = bfs(farthest_node)

        return distance_2
