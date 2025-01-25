class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        sums = [[0] * (n + 1) for _ in range(2)]

        # sums[0] represents the prefix of the top row, sums[1] is the prefix of the bottom row
        for i in range(1, n + 1):
            sums[0][i] = sums[0][i - 1] + grid[0][i - 1]
            sums[1][i] = sums[1][i - 1] + grid[1][i - 1]

        # here we use a prefix sum of n+1 size to avoid having to do edge cases for the start and end sequences.
        # it's a little confusing: when i = 0, we take the sum of the entire top row minus the leftmost element (L shape for red)
        # when we have the inverted L shape at i == n - 1, then we take the prefix sum of the bottom row for the first n-1 elements
        # this is stored at sums[1][n-1]; (sums[0][-1] - sums[0][n]) = 0

        blue = float("inf")
        for i in range(n):
            currentBlue = max(sums[0][-1] - sums[0][i + 1], sums[1][i])
            if currentBlue < blue:
                blue = currentBlue

        return blue
