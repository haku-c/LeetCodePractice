class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        res = None
        graph = defaultdict(list)
        # construct graph
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visitedB = {}

        # traverse to root from B
        def dfs(node, depth):
            if node == 0:
                return True

            visitedB[node] = depth

            for dest in graph[node]:
                if dest not in visitedB:
                    if dfs(dest, depth + 1):
                        return True

            del visitedB[node]

            return False

        dfs(bob, 0)

        # print(visitedB)
        # traverse to leaf node, modifying value as we go
        # reference if that node was met during our journey
        # (depth, node, currentCost)

        visitedA = set([0])
        path = deque([(0, 0, amount[0])])
        while path:
            depth, node, currentIncome = path.popleft()
            depth += 1
            leaf = True
            for dest in graph[node]:
                if dest not in visitedA:
                    if dest in visitedB and (depth > visitedB[dest]):
                        newIncome = currentIncome  # dont change income since B already opened gate
                    elif dest in visitedB and depth == visitedB[dest]:
                        newIncome = currentIncome + (
                            amount[dest] / 2
                        )  # A and B arrive at the same time
                    else:
                        newIncome = currentIncome + amount[dest]
                    leaf = False
                    visitedA.add(dest)
                    path.append((depth, dest, newIncome))
            if leaf:
                res = currentIncome if res is None else max(res, currentIncome)
        return int(res)


# do a dfs to get the path from b to root
# do bfs to traverse to all leaf nodes

# you can do this with 2 dfs, or 1 dfs as well (better memory)
