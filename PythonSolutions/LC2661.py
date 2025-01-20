class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [n] * m
        cols = [m] * n
        d = [(0, 0)] * (m * n)
        for i in range(m):
            for j in range(n):
                d[mat[i][j] - 1] = i, j

        for i in range(len(arr)):
            row, col = d[arr[i] - 1]
            rows[row] -= 1
            if rows[row] == 0:
                return i
            cols[col] -= 1
            if cols[col] == 0:
                return i
        return -1


# straightforward, use a dictionary or array to cache the locations of each value.
# then track the counts in each row or col
