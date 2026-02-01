# lc 419
class Solution:
    # TC: O(M * N) SC: O(1) M: 行数  N: 列数
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        rows, cols = len(board), len(board[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # 看看它左边有没有 X, 看看它上边有没有 X, 只有既没有左邻居，也没有上邻居的 X，才是战舰的“头”
                    if r > 0 and c > 0:
                        if board[r][c - 1] != 'X' and board[r - 1][c] != 'X':
                            count += 1
                    else:
                        if r == 0 and c == 0:
                            count += 1
                        elif r == 0:
                            if board[r][c - 1] != 'X':
                                count += 1
                        else:
                            if board[r - 1][c] != 'X':
                                count += 1
        
        return count                   

    # TC: O(M * N) SC: O(MAX(M, N)) M: 行数  N: 列数
    def countBattleshipsDFS(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        rows, cols = len(board), len(board[0])
        count = 0

        # 每个点其实查右和下两个方向就够了
        def flood_fill(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'X':
                return

            board[r][c] = 'Y'
            flood_fill(r, c + 1)
            flood_fill(r + 1, c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    flood_fill(i, j)
                    count += 1
        
        return count