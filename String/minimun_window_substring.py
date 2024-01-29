# lc 76
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ''
        
        count_t, window = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        
        # have 表示有多少对k，v满足和count_v里面的k，v
        # 满足意思就是v in have >= v in count_v for same k
        have, need = 0, len(count_t)
        l = 0
        res, res_len = [-1, -1], float('inf')
        for r in range(len(s)):
            c = s[r]
            if c in count_t:
                window[c] = 1 + window.get(c, 0)
                if window[c] == count_t[c]:
                    have += 1

                while have == need:
                    if (r - l + 1) < res_len:
                        res_len = r - l + 1
                        res = [l, r]
                    if s[l] in count_t:
                        window[s[l]] -= 1
                        if window[s[l]] < count_t[s[l]]:
                            have -= 1
                    l += 1  
        start, end = res
        return s[start:end + 1] if res_len != float('inf') else ''
        
s = Solution()
print(s.minWindow('ADOBECODEBANC', 'ABC'))