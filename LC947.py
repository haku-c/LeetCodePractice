from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [0] * n
        row = defaultdict(list)
        col = defaultdict(list)
        for i in range(n):
            currentRow, currentCol = stones[i]
            row[currentRow].append(i)
            col[currentCol].append(i)

        def traverse(index):
            if visited[index]:
                return
            currentRow, currentCol = stones[index]
            visited[index] = 1
            for r in row[currentRow]:
                traverse(r)
            for c in col[currentCol]:
                traverse(c)

        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                traverse(i)

        return n - components
