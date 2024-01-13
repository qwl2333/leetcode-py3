# 150

from math import floor, ceil

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = set({'+', '-', '*', '/'})
        for token in tokens:
            if token not in operators:
                num = int(token)
                stack.append(num)
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    num3 = num1 + num2
                elif token == '-':
                    num3 = num1 - num2
                elif token == '*':
                    num3 = num1 * num2
                else:
                    # int() can truncate towards 0, meaning int(-2.5) = -2, int(2.5) = 2
                    # num3 = int(num1 / num2)
                    num3 = floor(num1 / num2) if num1 / num2 > 0 else ceil(num1 / num2)

                stack.append(num3)
        
        return stack.pop()

a = Solution()
print(a.evalRPN(''))