# lc 424
# neetcode https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    # Time O(26n), Space O(26), 双指针，l r组成的substring的长度 - l,r之间最高freq出现的字母 <= k, 这个substring才符合要求
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        l, r = 0, 0
        max_len = 0
        while r < n:
            freq[s[r]] = freq.get(s[r], 0) + 1
            while (r - l + 1) - max(freq.values()) > k: # max(freq.values()) is O(26) since 26 upppercase letters
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len