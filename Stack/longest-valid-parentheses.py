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

    # t O(n) s O(n)
    def longestValidParenthesesDP(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [0 for _ in range(n)]
        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
        else:
            dp[1] = 0

        for i in range(2, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else: # s[i - 1] == ')':
                    if i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[i - 2 - dp[i - 1]] if i - 2 - dp[i - 1] >= 0 else 0)
        
        return max(dp)

s = Solution()
print(s.longestValidParentheses('))()(())'))