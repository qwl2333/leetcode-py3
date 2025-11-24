# lc 1249
# 和 lc 921 类似, 可以去看下 921里面的comments
class Solution:
    # T O(N), S O(1) 不考虑存放结果的array， 避免了使用stack，但是我觉得stack解法更简单,面试还是用stack解法
    # 和 lc 32最优解的解法很像
    def minRemoveToMakeValidNoStack(self, s: str) -> str:
        # --- 第一轮：从左往右，清理多余的 ')' ---
        first_pass = []
        left = 0
        right = 0
        
        for c in s:
            if c == '(':
                first_pass.append(c)
                left += 1
            elif c == ')':
                # 只有当有足够的左括号时，才保留这个右括号
                if right < left:
                    first_pass.append(c)
                    right += 1
                # 否则：说明这个 ')' 多余了，直接丢弃（不 append）
            else:
                first_pass.append(c)
        
        # --- 第二轮：从右往左，清理多余的 '(' ---
        # 现在的 first_pass 里，右括号肯定不多于左括号，但左括号可能多了 (比如 "(()")
        # 我们倒着看，逻辑完全反过来：把 ')' 当作资源，去匹配 '('
        
        result = []
        left = 0
        right = 0
        
        for c in reversed(first_pass):
            if c == ')':
                result.append(c)
                right += 1
            elif c == '(':
                # 只有当有足够的右括号时，才保留这个左括号
                if left < right:
                    result.append(c)
                    left += 1
                # 否则：说明这个 '(' 多余了，丢弃
            else:
                result.append(c)
                
        # 别忘了结果是倒着的，要翻回来
        return "".join(reversed(result))

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
