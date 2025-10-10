# lc 921 min 加几个 
# 与 1249 min 减去几个 类似
# 求min add to make valid parenthese 和 min remove to make valid parenthese
# 是一样的意思, 说得到的number of moves是一样的
# 但是 1249 用到stack是因为需要得到真正的修改之后的str, 必须记录要改变的位置在stack里面
class Solution:
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