# lc 32
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 利用stack记录idx，)的时候pop，然后计算substring的长度
        stack = list([-1]) # 一开始给一个假idx-1方便计算, stack存的是一个idx，[idx + 1, i]可以组成一个valid parentheses
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # 如果遇到))()，这种情况，-1被pop出来之后，要加入一个新的start index
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len

s = Solution()
print(s.longestValidParentheses('))()(())'))