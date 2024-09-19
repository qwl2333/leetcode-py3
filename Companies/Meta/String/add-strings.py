# lc 415
class Solution:
    # time O(n) space O(n)
    # 这题难点是 res用str存储而不是数字，因为如果数字很大，数字最后转换为str会报错
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        res = ''
        carry = 0
        count = 0
        while i >= 0 and j >= 0:
            temp_sum = int(num1[i]) + int(num2[j]) + carry
            res += str(temp_sum % 10)
            carry = temp_sum // 10
            count += 1
            i -= 1
            j -= 1
        
        while i >= 0:
            temp_sum = int(num1[i]) + carry
            res += str(temp_sum % 10)
            carry = temp_sum // 10
            count += 1
            i -= 1
        
        while j >= 0:
            temp_sum = int(num2[j]) + carry
            res += str(temp_sum % 10)
            carry = temp_sum // 10
            count += 1
            j -= 1

        if carry == 1:
            res += str(carry)
        
        return res[::-1]