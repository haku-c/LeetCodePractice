class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.prefix[i - 1][j]
                    + self.prefix[i][j - 1]
                    - self.prefix[i - 1][j - 1]
                )
        print(self.prefix)

    # because of the shift making the first row and the first col all 0s, you want to add 1 to the general formulas here.
    # this removes the need for checking for out of bound indexing when creating the prefix sum and when using it
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        num = self.prefix[row2 + 1][col2 + 1]
        upperSub = self.prefix[row1][col2 + 1]
        leftSub = self.prefix[row2 + 1][col1]
        add = self.prefix[row1][col1]
        return num - upperSub - leftSub + add


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
