class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # simple dfs cycle detection.
        # visited = [0] * n
        # def dfs(current, parent):
        #     if visited[current]:
        #         return True
        #     visited[current] = 1
        #     # print(current)
        #     for dest in graph[current]:
        #         if dest == parent:
        #             continue
        #         elif dfs(dest, current):
        #             return True
        #     return False

        # if dfs(0,-1):
        #     return False

        # # print(visited)
        # return sum(visited) == n

        # simple bfs solution
        visited = [0] * n
        q = deque([(0, -1)])
        visited[0] = 1
        while q:
            current, parent = q.popleft()
            for dest in graph[current]:
                if dest != parent:
                    if visited[dest]:
                        return False
                    visited[dest] = 1
                    q.append((dest, current))
        # print(visited)
        # graph needs to be connected. check if you can visit all nodes
        return all(visited)


# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.
