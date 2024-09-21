# lc 1249
class Solution:
    # time O(n), space O(n)
    # 重点是把s变成list，方便直接修改
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)

s = Solution()
print(s.minRemoveToMakeValid('lee(t(c)o)de)')) # expected lee(t(c)o)de
