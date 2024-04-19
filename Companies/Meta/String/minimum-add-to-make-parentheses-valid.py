# lc 921
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
                res += (count_close - count_open)
                count_open = count_close
        
        res += (count_open - count_close)
        return res

s = Solution()
print(s.minAddToMakeValid('))(('))