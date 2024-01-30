# lc 438
class Solution:
    # Time: O(n) - one pass over the p, on pass for s, and for every window (window of len(p)) in s, we iterate over values in hashmap (maximum 26)
    # Space: O(1) - hashmap with max 26 keys
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len = len(s)
        p_len = len(p)
        if p_len > s_len:
            return []
        res = []
        p_count = {}
        s_count = {}
        for i in range(p_len):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
        res = [0] if p_count == s_count else []
        l = 0
        for r in range(p_len, s_len):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                s_count.pop(s[l])
            l += 1
            if s_count == p_count:
                res.append(l)

        return res

s = Solution()
print(s.findAnagrams('cbaebabacd', 'abc'))
