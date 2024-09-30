# lc 48 要是忘记了，直接看neetcode的解法吧
class Solution:
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
s.rotate(input)
print(input)