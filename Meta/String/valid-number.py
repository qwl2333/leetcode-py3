# lc 65
class Solution:
    def is_unsigned_integer(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False

        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
        return True

    def is_integer(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False
    
        if s[start] == '+' or s[start] == '-':
            return self.is_unsigned_integer(s, start + 1, end)
        else:
            return self.is_unsigned_integer(s, start, end)

    def is_unsigned_decimal(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False
        count_dot = 0
        count_digits_before_dot = 0
        count_digits_after_dot = 0
        for i in range(start, end + 1):
            if s[i].isdigit():
                if count_dot == 0:
                    count_digits_before_dot += 1
                else:
                    count_digits_after_dot += 1
            elif s[i] == '.':
                count_dot += 1
                if count_dot > 1:
                    return False
            else:
                return False
        
        if count_dot == 1 and (count_digits_before_dot > 0 and count_digits_after_dot == 0) \
            or (count_digits_before_dot > 0 and count_digits_after_dot > 0) \
            or (count_digits_before_dot == 0 and count_digits_after_dot > 0):
            return True
        else:
            return False

    def is_decimal(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False

        if s[start] == '+' or s[start] == '-':
            return self.is_unsigned_decimal(s, start + 1, end)
        else:
            return self.is_unsigned_decimal(s, start, end)

    # Time O(n), space O(1)
    def isNumber(self, s: str) -> bool:
        for idx, c in enumerate(s):
            if c in 'eE':
                after_e = self.is_integer(s, idx + 1, len(s) - 1)
                before_e = self.is_integer(s, 0, idx - 1) or self.is_decimal(s, 0, idx - 1)
                return after_e and before_e

        return self.is_integer(s, 0, len(s) - 1) or self.is_decimal(s, 0, len(s) - 1)

s = Solution()
print(s.isNumber('95a54e53'))