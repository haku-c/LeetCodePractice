class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        borders = [n, m, -1, 0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction = 0
        currentRow, currentCol = 0, 0
        while len(res) < m * n:
            res.append(matrix[currentRow][currentCol])
            toggle = True
            # if we need to keep switching directions, do so
            while toggle:
                deltaX, deltaY = directions[direction]
                newRow, newCol = currentRow + deltaX, currentCol + deltaY
                if direction == 0 and newCol == borders[direction]:
                    newBound = newCol - 1
                elif direction == 2 and newCol == borders[direction]:
                    newBound = newCol + 1
                elif direction == 1 and newRow == borders[direction]:
                    newBound = newRow - 1
                elif direction == 3 and newRow == borders[direction]:
                    newBound = newRow + 1
                else:
                    toggle = False

                if toggle:
                    borders[direction] = newBound
                    direction = (direction + 1) % 4
                else:
                    currentRow, currentCol = newRow, newCol
        return res

    # the borders and the directions have the same indexing, i.e if you go down the corresponding bottom border is at the same index
