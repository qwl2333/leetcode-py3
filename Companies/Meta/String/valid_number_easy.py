# lc 65 meta 面试简单版本
# 原版本 + - . 没有Ee
# integer: optional +/- 和 digits
# decimal: optional +/- 和 1) digits, 2) digits.digits, 3) .digits
# examples: "22", "+22", "-22", "+1.09", "-0.9", "-.9", "+4.0", "+4."
#
class Solution:
    def isNumber(self, s: str) -> bool:
        return self.is_decimal(s, 0, len(s) - 1) or self.is_integer(s, 0, len(s) - 1)
    
    def is_integer(self, s: str, start: int, end: int) -> bool:
        if s[start] == '+' or s[start] == '-':
            return self.is_unsigned_integer(s, start + 1, end)
        else:
            return self.is_unsigned_integer(s, start, end)
        
    def is_unsigned_integer(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False

        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
        return True
    
    def is_decimal(self, s: str, start: int, end: int) -> bool:
        if s[start] == '+' or s[start] == '-':
            return self.is_unsigned_decimal(s, start + 1, end)
        else:
            return self.is_unsigned_decimal(s, start, end)

    def is_unsigned_decimal(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False

        count_before_dot = 0
        count_after_dot = 0
        count_dot = 0
        for i in range(start, end + 1):
            if s[i] == '.':
                count_dot += 1
                if count_dot > 1:
                    return False
            elif s[i].isdigit():
                if count_dot == 0:
                    count_before_dot += 1
                else:
                    count_after_dot += 1
            else:
                return False
        if count_dot == 1 and \
        ((count_before_dot > 0 and count_after_dot > 0) or \
        (count_before_dot == 0 and count_after_dot > 0) or \
        (count_before_dot > 0 and count_after_dot == 0)):
            return True
        else:
            return False

s = Solution()
print(s.isNumber('-4.'))  
