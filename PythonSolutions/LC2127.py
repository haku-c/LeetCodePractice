class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        distances = [0] * n
        cyclePoints = [-1] * n
        self.res = 0

        def dfs(currentNode, currentLength, seen, last):
            # cycle detected
            if seen[currentNode] != -1:
                if seen[currentNode] == currentLength - 1:
                    # length 2 cycle
                    cyclePoints[currentNode] = last
                    cyclePoints[last] = currentNode
                    distances[last] = 1
                    distances[currentNode] = currentLength - 1
                    return
                else:
                    # cycle of another length
                    self.res = max(self.res, currentLength - seen[currentNode] + 1)
                    return

            currentLength += 1
            distances[currentNode] = currentLength
            seen[currentNode] = currentLength

            if cyclePoints[currentNode] != -1:
                return

            destination = favorite[currentNode]
            if distances[destination] < currentLength + 1:
                dfs(destination, currentLength, seen, currentNode)

        for i in range(n):
            if distances[i] == 0:
                dfs(i, 0, [-1] * n, i)

        cycles = 0
        for i in range(n):
            if cyclePoints[i] != -1 and cyclePoints[i] > i:
                cycles += distances[cyclePoints[i]] + distances[i]
                self.res = max(self.res, cycles)

        return self.res


# this code TLEs. It's not O(n) because it might retraverse already found nodes since it calls dfs from 0 to n nodes.
# generally, dfs is slower than bfs in python, which i think is another factor
# the code does work on smaller inputs, and the logic is sound.

# an idea to take from the solution is to use the reverse graph when you get a length 2 cycle and expand from the two points to
# find the longest paths to either end of the length 2 cycle.
# this reduces recomputation
