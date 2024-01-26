# lc 242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
        
        for char in t:
            if char not in map:
                return False
            else:
                map[char] -= 1
        
        for v in map.values():
            if v != 0:
                return False
        
        return True

s = Solution()
print(s.isAnagram('rat', 'car'))
        
        