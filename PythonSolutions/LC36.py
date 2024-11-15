class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # check rows
        for i in range(9):
            seen.clear()
            for j in range(9):
                current = board[i][j]
                if current in seen:
                    return False
                elif current != ".":
                    seen.add(current)
        for j in range(9):
            seen.clear()
            for i in range(9):
                current = board[i][j]
                if current in seen:
                    return False
                elif current != ".":
                    seen.add(current)
        centers = [
            [1, 1],
            [4, 1],
            [7, 1],
            [1, 4],
            [1, 7],
            [4, 4],
            [4, 7],
            [7, 4],
            [7, 7],
        ]
        directions = [
            [1, 1],
            [1, 0],
            [0, 1],
            [-1, -1],
            [-1, 0],
            [1, -1],
            [0, -1],
            [-1, 1],
            [0, 0],
        ]
        for x, y in centers:
            seen.clear()
            for delX, delY in directions:
                current = board[x + delX][y + delY]
                if current in seen:
                    return False
                elif current != ".":
                    seen.add(current)
        return True
