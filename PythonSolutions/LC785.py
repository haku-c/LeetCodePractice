from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0:
                colors[i] = -1
                queue = deque([(-1, i)])
                while queue:
                    color, current = queue.popleft()
                    for dest in graph[current]:
                        if colors[dest] == 0:
                            # setting the color in the previous iteration is much faster
                            colors[dest] = -1 * color
                            queue.append((-1 * color, dest))
                        elif colors[dest] != (-1 * color):
                            return False
        return True
