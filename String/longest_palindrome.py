# lc 409
import math
class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = {}
        even_char = set()
        res = 0

        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
            if map[char] % 2 == 1:
                even_char.add(char)
            else:
                if char in even_char:
                    even_char.remove(char)

        if even_char:
            first = even_char.pop()
            res += map[first]
            del map[first]

        for v in map.values():
            res += math.floor(v / 2) * 2
        
        return res
    
    # 上面解法简化版
    # 不需要一个set来记录出现奇数频率的character，一个odd_count记录几个character出现奇数次就够了
    # 同时，因为所有奇数次的character只能选一个当中心，其他都当偶数次character了，
    # 所以回文串长度就是len(s) - odd_count + 1， 比如‘abbbfccccdd’ a，b，f是奇数的出现了1，3，1次数
    # odd_count是3因为有三个奇数次的character，只能选一个为中心, 其他舍弃
    # 所以一定要舍弃掉（odd_count - 1）两个，res = 11 - 2 = 9
    def longestPalindrome2(self, s: str) -> int:
        odd_count = 0
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)

s = Solution()
print(s.longestPalindrome2('abbbfccccdd'))
            
        