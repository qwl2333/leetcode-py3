# lc 66 和 lc 369 类似
class Solution:
    '''
    第一反应算进位
    new_num = (digits[i] + 1 + carry) % 10
    carry = (digits[i] + 1 + carry) // 10

    但是聪明做法是只判断最后一个是不是小于9, 小于9可以加1后直接返回
    如果等于9, 就是继续往前处理plusOne

    TC: O(n) worst case需要遍历整个数组, 最好情况O(1), 只处理最后一位, 小于9时
    SC: O(1) 一般是在原数组修改, 除非[9,9,9,9..]的情况需要开辟额外 n+1 空间
    '''
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # 从右向左遍历（从低位到高位）
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # 只要当前位不到 9，加 1 之后不会产生进位，直接结束
                digits[i] += 1
                return digits
            
            # 如果是 9，加 1 变成 10，当前位设为 0，继续循环处理前一位
            digits[i] = 0
            
        # 如果循环走完还没 return，说明最高位也产生了进位（如 999 -> 000）
        # 我们需要在最前面补一个 1
        return [1] + digits