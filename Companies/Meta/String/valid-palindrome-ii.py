# lc 680
class Solution:
    # Time O(n), space O(1)
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def validPalindromeHelper(l: int, r: int, s: str) -> bool:
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # skip l
                skip_left = validPalindromeHelper(l + 1, r, s)
                # skip r
                skip_right = validPalindromeHelper(l, r - 1, s)
                return skip_left or skip_right
        return True