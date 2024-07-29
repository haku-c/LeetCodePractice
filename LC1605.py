def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    res = [[0] * len(colSum) for i in range(len(rowSum))]
    while not all(x == 0 for x in rowSum) and not all(x == 0 for x in colSum):
        minRow, minRowIndex = min(
            (val, ind) for ind, val in enumerate(rowSum) if val > 0
        )
        minCol, minColIndex = min(
            (val, ind) for ind, val in enumerate(colSum) if val > 0
        )
        sub = min(minRow, minCol)
        res[minRowIndex][minColIndex] = sub
        rowSum[minRowIndex] -= sub
        colSum[minColIndex] -= sub
    return res
