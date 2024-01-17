# lc 224
class Solution:
    def calculate(self, s: str) -> int:
        stack: list[str] = []
        for char in s:
            if char == ' ':
                continue
            if char == ')':
                sum = self.calculate_for_parenthese(stack)
                stack.append(str(sum))
                continue

            stack.append(char)
            
        print(stack)
        return self.calculate_for_parenthese(stack)
    
    # (1-2+3) or 1 - 2 + 3 
    def calculate_for_parenthese(self, stack: list) -> int:
        if stack and stack[-1] == ')':
            stack.pop()

        prev_num = 0
        count = 0
        sum = 0
        while stack and stack[-1] != '(':
            while stack and (stack[-1].isdigit() or (stack[-1][0] == '-' and stack[-1][1:].isdigit())):
                num = int(stack.pop())
                prev_num = 10 ** count * num + prev_num
                count += 1
            if stack and stack[-1] == '+':
                stack.pop()
                sum += prev_num
                prev_num = 0
                count = 0
            if stack and stack[-1] == '-':
                stack.pop()
                sum += prev_num * -1
                prev_num = 0
                count = 0

        if stack and stack[-1] == '(':
            stack.pop()

        sum += prev_num
        return sum

a = Solution()
print(a.calculate('1-(     -2)'))