# lc 48 要是忘记了，直接看neetcode的解法吧
class Solution:
    '''
    这个解法最好记
    transpose then reverse each row
    TC O(N^2)
    SC O(1)
    '''
    def rotate1(self, matrix: list[list[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            n = len(matrix)
            
            # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
            # We only iterate through the upper triangle (j > i) to avoid double-swapping
            for i in range(n):
                for j in range(i + 1, n):
                    print(f'i:{i}, j:{j}')
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # Step 2: Reverse each row
            for i in range(n):
                matrix[i].reverse()

    # Time O(n^2), Space O(1)
    '''
    一圈一圈的从外往内rotate
    '''
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1 # 0, 3
        while l < r:
            for i in range(r - l): # 一圈里面, 从matrix[0][l]到matrix[0][r-1]都需要rotate, matrix[0][r]不需要因为已经被matrix[0][l]占据了
                top, bottom = l, r
                top_left = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left
            r -= 1
            l += 1

s = Solution()
input = [[5,1,9,11],
         [2,4,8,10],
         [13,3,6,7],
         [15,14,12,16]]
s.rotate1(input)
print(input)