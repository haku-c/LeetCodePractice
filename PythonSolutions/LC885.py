class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        res.append([rStart, cStart])
        ind = 1
        direction = 0
        currentRow = rStart
        currentCol = cStart
        mult = 1
        while len(res) < rows * cols:
            for j in range(2):
                for i in range(mult):
                    currentRow = currentRow + directions[direction][0]
                    currentCol = currentCol + directions[direction][1]
                    if (
                        currentRow >= 0
                        and currentRow < rows
                        and currentCol < cols
                        and currentCol >= 0
                    ):
                        res.append([currentRow, currentCol])
                direction = (direction + 1) % 4
            mult += 1
        return res
