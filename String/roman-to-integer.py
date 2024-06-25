# lc 13
# neetcode 讲的很好
class Solution:
    # TIme O(n) - n is len(s), space O(1)
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i,c in enumerate(s):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

s = Solution()
print(s.romanToInt('CMXCVIII'))