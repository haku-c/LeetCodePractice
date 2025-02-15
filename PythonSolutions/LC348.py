class TicTacToe:

    def __init__(self, n: int):
        # self.board = [[0] * n for _ in range(n)]
        self.n = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag = [[0, 0] for _ in range(n)]
        self.ltr = set([(i, i) for i in range(self.n)])
        self.rtl = set([(i, n - 1 - i) for i in range(n)])
        self.diag = [[0, 0], [0, 0]]

    # def checkDiag(self, player):
    #         ltr = [self.board[i][i] for i in range(self.n)].count(player) == self.n
    #         rtl = [self.board[i][self.n - 1 - i] for i in range(self.n)].count(player) == self.n
    #         return ltr or rtl

    def move(self, row: int, col: int, player: int) -> int:
        # self.board[row][col] = player
        self.rows[row][player - 1] += 1
        self.cols[col][player - 1] += 1
        if (row, col) in self.ltr:
            self.diag[0][player - 1] += 1
        if (row, col) in self.rtl:
            self.diag[1][player - 1] += 1

        if (
            self.rows[row][player - 1] == self.n
            or self.cols[col][player - 1] == self.n
            or self.diag[1][player - 1] == self.n
            or self.diag[0][player - 1] == self.n
        ):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# you can store counts of the rows, 2 diagonals, and cols and check (instead of reiterating over the board again)
