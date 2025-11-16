# lc 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower() # space need O(n)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): # isalnum = is alphanumeric 字母+数字
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True
                
s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))      
