# lc 498
# https://leetcode.com/problems/diagonal-traverse/solutions/97711/java-15-lines-without-using-boolean/

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        n = len(mat)
        m = len(mat[0])
        r, c = 0, 0
        res = [0 for _ in range(n * m)]
        for i in range(n * m):
            res[i] = mat[r][c]
            if (r + c) % 2 == 0: # move right up
                if c == m - 1: # 顺序不可调换，必须先check c有没有到最右,如果先check r, 在增加c时，有可能c已经到最右了c就出界了
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else: # move left down
                if r == n - 1: # 同理如果先check c==0 可能会出现r出界的情况
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return res