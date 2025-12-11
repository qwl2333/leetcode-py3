# lc 240
class Solution:
    # tc O(m + n)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        cur_r = M - 1
        cur_c = 0
        while cur_r >= 0 and cur_c < N:
            if matrix[cur_r][cur_c] == target:
                return True
            elif matrix[cur_r][cur_c] > target:
                cur_r -= 1
            else:
                cur_c += 1
        
        return False