# lc 1047 和 lc 1209类似
class Solution:
    # ai的sol就是比较elegant
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)

    # 我的sol比较笨比
    def removeDuplicatesMySol(self, s: str) -> str:
        stack = []
        size = len(s)
        i = 0
        while i < size:
            if not stack:
                stack.append(s[i])
                i += 1
                continue
            while i < size and stack and stack[-1] == s[i]:
                stack.pop()
                i += 1
            if i < size:
                stack.append(s[i])
                i += 1
        return ''.join(stack)