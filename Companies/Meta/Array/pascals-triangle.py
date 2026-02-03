# lc 118
class Solution:
    # TC O(n ^ 2) 1 + 2 ... + n   SC O(n) 最后一层需要的空间是n n就是numRows
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = res[i - 1]
            new = [1] * (i + 1)
            for j in range(len(new)):
                if j == 0 or j == len(new) - 1:
                    continue
                new[j] = prev[j - 1] + prev[j]
            res.append(new)
        
        return res