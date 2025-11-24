# lc 921 min 加几个 
# 与 1249 min 减去几个 类似
# 求min add to make valid parenthese 和 min remove to make valid parenthese
# 是一样的意思, 说得到的number of moves是一样的
# 但是 1249 用到stack是因为需要得到真正的修改之后的str, 必须记录要改变的位置在stack里面
class Solution:
    # T O(N), S O(1) 不考虑存放结果的array， 避免了使用stack
    # 和 lc 32最优解的解法很像
    def minRemoveToMakeValid(self, s: str) -> str:
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

    # Time O(n), space O(1)
    def minAddToMakeValid(self, s: str) -> int:
        count_left = 0
        count_right = 0
        res = 0
        for c in s:
            if c == '(':
                count_left += 1
            else:
                count_right += 1
                if count_left < count_right:
                    res += 1 # res += (count_right - count_left) this means we need to add
                            # a (, to make sure count_left and count_right are equal
                    count_left = count_right
        
        res += (count_left - count_right)
        return res

s = Solution()
print(s.minAddToMakeValid('))(('))