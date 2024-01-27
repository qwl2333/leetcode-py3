# lc 8
class Solution:
    def myAtoi(self, s: str) -> int:
        started = False
        sign_found = False
        digit_found = False
        sign = 0
        res = 0
        for c in s:
            if not started and c == ' ':
                continue
          
            started = True
            if not sign_found and (c == '+' or c == '-') and not digit_found:
                sign_found = True
                sign = 1 if c == '+' else -1
                continue
            
            if c.isdigit():
                digit_found = True
                num = int(c)
                res = res * 10 + num
                continue
            else:
                break
        
        if sign_found:
            res = res * sign
        
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < - 2 ** 31:
            res = - 2 ** 31
        
        return res
        
s = Solution()
print(s.myAtoi('00000-42a1234'))