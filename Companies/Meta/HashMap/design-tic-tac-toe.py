class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows_counter = [0 for _ in range(n)]
        self.cols_counter = [0 for _ in range(n)]
        self.dia_counter = [0 for _ in range(2)]
        
    # 每一次move都保证是valid的,并且一定放在空格上，这个先决条件保证了无需check board满了没满
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            value = 1
        else:
            value = -1

        self.rows_counter[row] += value
        self.cols_counter[col] += value
        if row == col:
            self.dia_counter[0] += value
        if col == self.n - 1 - row:
            self.dia_counter[1] += value
        if (abs(self.rows_counter[row]) == self.n
            or abs(self.cols_counter[col]) == self.n
            or abs(self.dia_counter[0]) == self.n
            or abs(self.dia_counter[1]) == self.n):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)