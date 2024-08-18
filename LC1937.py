class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        opt = [[0] * n for i in range(2)]
        left = [0] * n
        right = [0] * n
        opt[0] = list(points[0])
        for row in range(1, m):
            pastBest = 0
            for col in range(n):
                pastBest = max(pastBest - 1, opt[0][col])
                left[col] = pastBest
            for col in reversed(range(n)):
                pastBest = max(pastBest - 1, opt[0][col])
                right[col] = pastBest
            for col in range(n):
                opt[1][col] = max(left[col], right[col]) + points[row][col]
            opt[0] = list(opt[1])
        return max(opt[0])
