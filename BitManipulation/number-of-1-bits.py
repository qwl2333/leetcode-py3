# lc 191
class Solution:
    # time 0(32) n is a 32 digit number
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n & 1
            n = n >> 1 # 相当于 n // 2
        return count