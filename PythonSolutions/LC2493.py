from collections import defaultdict, deque


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        self.res = 0

        # create the adjacency list graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        colors = [0] * (n + 1)

        # test if the component is bipartite
        def bipartite(node):
            colors[node] = -1
            queue = deque([(-1, node)])
            while queue:
                color, current = queue.popleft()
                for dest in graph[current]:
                    if colors[dest] == 0:
                        colors[dest] = -1 * color
                        queue.append((-1 * color, dest))
                    elif colors[dest] != (-1 * color):
                        return False
            return True

        # find the longest path in the connected component starting from node
        def depth(node):
            visited = [0] * (n + 1)
            visited[node] = True
            queue = deque([(1, node)])
            depth = 1
            while queue:
                currentDepth, currentNode = queue.popleft()
                for dest in graph[currentNode]:
                    if not visited[dest]:
                        depth = max(depth, currentDepth + 1)
                        visited[dest] = True
                        queue.append((currentDepth + 1, dest))
            return depth

        # in a connected component, find the longest path between any two nodes.
        def max_per_component(node, visited):
            visited[node] = True
            currentMax = distances[node]
            for dest in graph[node]:
                if not visited[dest]:
                    currentMax = max(max_per_component(dest, visited), currentMax)
            return currentMax

        # because we have a low number of nodes, we can do the bfs on every node.
        distances = [0] * (n + 1)
        for i in range(1, n + 1):
            distances[i] = depth(i)

        visitedNodeComponent = [0] * (n + 1)

        # iterate through all connected components. If we ever encounter an odd cycle, return -1. Otherwise, traverse the connected component and
        # add the longest path between any two nodes in the component to the result
        for i in range(1, n + 1):
            if colors[i] == 0:
                if bipartite(i):
                    self.res += max_per_component(i, visitedNodeComponent)
                else:
                    return -1

        return self.res
