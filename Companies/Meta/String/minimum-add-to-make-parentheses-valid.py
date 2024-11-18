# lc 921 min 加几个 
# 与 1249 min 减去几个 类似
# 求min add to make valid parenthese 和 min remove to make valid parenthese
# 是一样的意思, 说得到的number of moves是一样的
# 但是 1249 用到stack是因为需要得到真正的修改之后的str, 必须记录要改变的位置在stack里面
class Solution:
    # Time O(n), space O(1)
    def minAddToMakeValid(self, s: str) -> int:
        count_open = 0
        count_close = 0
        res = 0
        for c in s:
            if c == '(':
                count_open += 1
            else:
                count_close += 1
            if count_open < count_close:
                res += (count_close - count_open) # res += 1
                count_open = count_close
        
        res += (count_open - count_close)
        return res

s = Solution()
print(s.minAddToMakeValid('))(('))