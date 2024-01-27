# lc 5
class Solution:
    # brute force: time O(n^2), space O(1)
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        max_len = 0
        start = 0
        for i in range(size):
            j = 0
            while i - j >= 0 and i + j < size and s[i - j] == s[i + j]:
                if 2 * j + 1 > max_len:
                    max_len = 2 * j + 1
                    start = i - j
                j += 1
        
        for i in range(1, size):
            j = 0
            while s[i - 1] == s[i] and i - 1 - j >= 0 and i + j < size and s[i - 1 - j] == s[i + j]:
                if 2 * j + 2 > max_len:
                    max_len = 2 * j + 2
                    start = i - 1 - j
                j += 1
        
        return s[start : start + max_len]
    
s = Solution()
print(s.longestPalindrome('babad'))
            
