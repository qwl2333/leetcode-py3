# lc 680
class Solution:
    # Time O(n), space O(n)
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                string1 = s[:l] + s[l + 1:] # create a new string takes O(n) time
                string2 = s[:r] + s[r + 1:]
                return string1 == string1[::-1] or string2 == string2[::-1]
        return True

s = Solution()
print(s.validPalindrome('abbca'))