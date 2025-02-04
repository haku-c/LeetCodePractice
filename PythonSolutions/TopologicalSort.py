from collections import defaultdict, deque


def topological(nums):
    n = len(nums)
    indegrees = [0] * n
    graph = defaultdict(list)
    for i in range(n):
        destination = nums[i]
        indegrees[destination] += 1
        graph[i].append(destination)
    queue = deque()
    for i in range(n):
        if indegrees[i] == 0:
            queue.append(i)
    while queue:
        current = queue.popleft()
        for dest in graph[current]:
            indegrees[dest] -= 1
            if indegrees[dest] == 0:
                queue.append(dest)
        graph[current] = []
    print(graph)
