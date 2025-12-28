# lc 73
class Solution:
    '''
    题目就是如果matrix[i][j]为0 把这i行和j列都清零
    容易想到的解法是 用两个数组来记录行和列是不是有0 sc O(n + m)
    下面解法是 sc O(1) tc O(n * m)
    思路是用第一行和第一列来记录里面的内部的数组有没有0的
    '''
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row0_has_zero = False
        col0_has_zero = False

        # 1. 检查首行和首列是否原本就有 0
        for r in range(n):
            if matrix[r][0] == 0:
                col0_has_zero = True

        for c in range(m):
            if matrix[0][c] == 0:
                row0_has_zero = True
        
        # 2. 用第一行和第一列记录内部元素的 0 状态
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # 3. 根据第一行和第一列的标记，将内部元素置零
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # 4. 最后根据初始标志位处理第一行和第一列
        if col0_has_zero:
            for r in range(1, n):
                matrix[r][0] = 0
        
        if row0_has_zero:
            for c in range(1, m):
                matrix[0][c] = 0
                
                