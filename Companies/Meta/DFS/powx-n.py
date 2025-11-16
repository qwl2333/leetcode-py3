# lc 50
class Solution:
    # Time O(logn), space O(1)
    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        # Handle case where, n < 0.
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        # Perform Binary Exponentiation.
        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        return result

    # Time O(logn), space O(logn)
    def myPow(self, x: float, n: int) -> float:
        def myPowHelper(x: float, n: int) -> float:
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