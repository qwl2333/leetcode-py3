# lc 5
class Solution:
    # brute force: time O(n^2), space O(1)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_len = 0

        def extend_center(l: int, r: int):
            nonlocal start, max_len
            while l >= 0 and r < n and s[l] == s[r]:
                '''
                    record max_len and start first in case after l, r updated, they are out of line
                '''
                if max_len < r - l - 1:
                    max_len = r - l - 1
                    start = l + 1
                l -= 1
                r += 1

        for i in range(n):
            extend_center(i, i) # for palindromic substring with odd length
            if i < n - 1:
                extend_center(i, i + 1) # for palindromic substring with even length
        
        return s[start: start + max_len]
        
    
    # O(n^3) brute force
    def longestPalindromeBF(self, s: str):
        n = len(s)
        max_len = 0
        start = 0
        def is_palindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True

        for i in range(n):
            for j in range(i + 1, n + 1):
                if is_palindrome(s[i:j]):
                    if max_len < j - i:
                        max_len = j - i
                        start = i

        return s[start: start + max_len]


    
s = Solution()
print(s.longestPalindrome('babad'))
'''
abc
a
ab
abc
b
bc
c
'''