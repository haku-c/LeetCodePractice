# this question is just a 1d search since the sorting order degenerates the 2d array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while start <= end:
            current = start + (end - start) // 2
            row = int(current / n)
            col = current % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                start = current + 1
            else:
                end = current - 1
        return False
