# lc 70
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        last_two = 1
        last_one = 2
        for i in range(3, n + 1):
            cur = last_two + last_one
            last_two = last_one
            last_one = cur
        
        return last_one