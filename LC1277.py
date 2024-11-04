# when constructing the prefix sum you can avoid the checks for whether or not the index is less than zero or not by starting from 1 and going to m+1 or n+1
# this means you don't have to have edge case detection setting up your prefix sum matrix
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefixSum = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefixSum[i][j] = (
                    matrix[i - 1][j - 1]
                    + prefixSum[i - 1][j]
                    + prefixSum[i][j - 1]
                    - prefixSum[i - 1][j - 1]
                )
        res = 0
        limit = min(n, m)
        for upperRow in range(1, m + 1):
            for upperCol in range(1, n + 1):
                for i in range(limit):
                    lowerRow = upperRow + i
                    lowerCol = upperCol + i
                    if lowerRow >= m + 1 or lowerCol >= n + 1:
                        break
                    # general formula is [lowerRow, lowerCol] - [lowerRow, upperCol-1] - [upperRow - 1, lowerCol] + [upperRow - 1, upperCol -1]
                    num = prefixSum[lowerRow][lowerCol]
                    leftUpperAdd = prefixSum[upperRow - 1][upperCol - 1]
                    leftSub = prefixSum[lowerRow][upperCol - 1]
                    upperSub = prefixSum[upperRow - 1][lowerCol]
                    currentSum = num - leftSub - upperSub + leftUpperAdd
                    if currentSum == (i + 1) ** 2:
                        res += 1

        return res


# you can compare the code here
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         m = len(matrix)
#         n = len(matrix[0])
#         prefixSum = [[0] * n for i in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     prefixSum[i][j] = matrix[i][j]
#                 elif i > 0 and j == 0:
#                     prefixSum[i][j] = matrix[i][j] + prefixSum[i-1][0]
#                 elif j > 0 and i == 0:
#                     prefixSum[i][j] = matrix[i][j] + prefixSum[0][j-1]
#                 else:
#                     prefixSum[i][j] = matrix[i][j] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
#         res = 0
#         limit = min(n,m)
#         for upperRow in range(m):
#             for upperCol in range(n):
#                 for i in range(limit):
#                     lowerRow = upperRow + i
#                     lowerCol = upperCol + i
#                     if lowerRow >= m or lowerCol >= n:
#                         break
#                     # general formula is [lowerRow, lowerCol] - [lowerRow, upperCol-1] - [upperRow - 1, lowerCol] + [upperRow - 1, upperCol -1]
#                     num = prefixSum[lowerRow][lowerCol]
#                     leftSub = upperSub = leftUpperAdd = 0
#                     if upperCol > 0 and upperRow > 0:
#                         leftUpperAdd = prefixSum[upperRow - 1][upperCol - 1]
#                     if upperCol > 0:
#                         leftSub = prefixSum[lowerRow][upperCol - 1]
#                     if upperRow > 0:
#                         upperSub = prefixSum[upperRow - 1][lowerCol]

#                     currentSum = num - leftSub - upperSub + leftUpperAdd
#                     if currentSum == (i+1) ** 2:
#                         res += 1

#         return res
