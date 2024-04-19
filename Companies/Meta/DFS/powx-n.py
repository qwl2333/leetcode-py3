# lc 50
class Solution:
    # Time O(logn), space O(logn)
    def myPow(self, x: float, n: int) -> float:
        def myPowHelper(x: float, n: int):
            if n == 1:
                return x
            half = myPowHelper(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n > 0:
            return myPowHelper(x, n)
        elif n == 0:
            return 1
        else: # n < 0
            return 1/myPowHelper(x, -n)

s = Solution()
print(s.myPow(2.0, 9))