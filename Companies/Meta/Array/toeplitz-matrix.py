# lc 766
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        
        return True

    # 另一种解法是利用对角线的遍历
    def traverse_diagonals(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        
        # 所有的起点：第一列和第一行
        starts = []
        for c in range(cols - 1, 0, -1):
            starts.append((0, c))
        for r in range(rows):
            starts.append((r, 0))
        
        for r, c in starts:
            diag = []
            while r < rows and c < cols:
                diag.append(matrix[r][c])
                r += 1
                c += 1
            print(diag)

s = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
s.traverse_diagonals(matrix)