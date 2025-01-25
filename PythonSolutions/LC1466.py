from collections import deque, defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [0] * n
        queue = deque()
        graph = defaultdict(list)
        for source, destination in connections:
            graph[source].append((destination, 0))
            graph[destination].append((source, 1))
        # print(graph)
        res = 0
        queue.append(0)
        while queue:
            current = queue.popleft()
            visited[current] = 1
            for destination, way in graph[current]:
                if not visited[destination]:
                    if way == 0:
                        res += 1
                    queue.append(destination)
        return res


# bfs solution: you need to eventually visit every single city. If the edge is flipped the wrong way, increment
