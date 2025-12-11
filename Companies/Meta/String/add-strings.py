# lc 415
# 和 lc 2 add two numbers类似
class Solution:
    # time O(n) space O(n)
    # 这题难点是 res用str存储而不是数字，因为如果数字很大，数字最后转换为str会报错
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0:
            v1 = 0
            v2 = 0
            if i >= 0:
                v1 = int(num1[i])
                i -= 1
            if j >= 0:
                v2 = int(num2[j])
                j -= 1
            temp_sum = v1 + v2 + carry
            res += str(temp_sum % 10)
            carry = temp_sum // 10

        if carry == 1:
            res += str(carry)