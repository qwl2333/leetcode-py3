# lc 1249
# 和 lc 921 类似, 可以去看下 921里面的comments
class Solution:
    # time O(n), space O(n)
    # 重点是把s变成list，方便直接修改
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = [] # 记录多余的(
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = '' # 多余的)在这就被处理掉了
        while stack:
            s[stack.pop()] = '' # 处理记录下来的多余的(
        return ''.join(s)

s = Solution()
print(s.minRemoveToMakeValid('lee)t)c(o(de)')) # expected leetco(de)
