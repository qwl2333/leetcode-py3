# lc 231
class Solution:
    # TC O(logN) 每次砍掉一半  SC O(logN) stack
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: # 非常容易忽略的停止条件
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        else:
            return False

    # TC O(logN) 每次砍掉一半  SC O(1)
    def isPowerOfTwo_iterative(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n //= 2  # 缩写，等同于 n = n // 2
            
        return n == 1 # 如果n % 2 != 0, n是个别的奇数7或者3, 都不可以