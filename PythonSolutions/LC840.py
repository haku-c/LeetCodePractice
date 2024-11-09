class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check(grid, top, start, valid):
            if not (
                valid[top, start]
                and valid[top, start + 1]
                and valid[top, start + 2]
                and valid[top + 1, start]
                and valid[top + 1, start + 1]
                and valid[top + 1, start + 2]
                and valid[top + 2, start]
                and valid[top + 2, start + 1]
                and valid[top + 2, start + 2]
            ):
                return False
            uni = set()
            uni.add(grid[top][start])
            uni.add(grid[top][start + 1])
            uni.add(grid[top][start + 2])
            uni.add(grid[top + 1][start])
            uni.add(grid[top + 1][start + 1])
            uni.add(grid[top + 1][start + 2])
            uni.add(grid[top + 2][start])
            uni.add(grid[top + 2][start + 1])
            uni.add(grid[top + 2][start + 2])
            return len(uni) == 9

        def checkDiag(grid, top, start):
            sumLR = (
                grid[top][start] + grid[top + 1][start + 1] + grid[top + 2][start + 2]
            )
            sumRL = (
                grid[top + 2][start] + grid[top + 1][start + 1] + grid[top][start + 2]
            )
            return sumLR == sumRL

        if len(grid[0]) < 3 or len(grid) < 3:
            return 0
        rSum = {}
        cSum = {}
        ind = 0
        valid = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                valid[i, j] = grid[i][j] >= 1 and grid[i][j] <= 9
        while ind < len(grid):
            rSum[ind, 0, 2] = sum(grid[ind][0:3])
            start = 1
            end = 3
            while end < len(grid[0]):
                rSum[ind, start, end] = (
                    rSum[ind, start - 1, end - 1]
                    + grid[ind][end]
                    - grid[ind][start - 1]
                )
                start += 1
                end += 1
            ind += 1
        ind = 0
        while ind < len(grid[0]):
            cSum[ind, 0, 2] = sum([row[ind] for row in grid][0:3])
            start = 1
            end = 3
            while end < len(grid):
                cSum[ind, start, end] = (
                    cSum[ind, start - 1, end - 1]
                    + grid[end][ind]
                    - grid[start - 1][ind]
                )
                start += 1
                end += 1
            ind += 1
        topRowNum = 0
        res = 0

        while topRowNum + 2 < len(grid):
            start = 0
            end = 2
            while end < len(grid[0]):
                topRow = rSum[topRowNum, start, end]
                middleRow = rSum[topRowNum + 1, start, end]
                bottomRow = rSum[topRowNum + 2, start, end]
                leftCol = cSum[start, topRowNum, topRowNum + 2]
                middleCol = cSum[start + 1, topRowNum, topRowNum + 2]
                rightCol = cSum[end, topRowNum, topRowNum + 2]
                if (
                    check(grid, topRowNum, start, valid)
                    and topRow == middleRow
                    and bottomRow == middleRow
                    and leftCol == topRow
                    and middleCol == rightCol
                    and middleCol == leftCol
                    and checkDiag(grid, topRowNum, start)
                ):
                    res += 1
                start += 1
                end += 1

            topRowNum += 1

        return res
