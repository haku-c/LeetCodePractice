class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # O(m^2n^2)
        # O(2mn)
        # Don't want to overcount or undercount, but 1 invalid server is both the sole server in one row and one column
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        locations = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    locations.append((i, j))
        total = len(locations)
        for index in range(len(locations)):
            i, j = locations[index]
            if rows[i] == 1 and cols[j] == 1:
                total -= 1
        return total


# uses O(m + n + # servers) space -> O(mn)
# performance is O(mn + # servers), we iterate over ever server to check if it's the only one in that row
# since m and n are rather small, we can take this approach -> number servers bounded by m*n
# we can also iterate over all cells again instead of logging just the cell ids with servers.
