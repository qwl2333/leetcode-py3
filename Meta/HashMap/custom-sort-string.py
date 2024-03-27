# lc 791
class Solution:
    # Time O(n), Space O(n) n - length of s
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        res = ''
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in order:
            if c in freq:
                for _ in range(freq[c]):
                    res += c
                del freq[c]

        for k, v in freq.items():
            for _ in range(v):
                res += k
        
        return res

    # Time O(nlogn + 26) dic has at most 26 keys, Space O(n)  n - length of s
    def customSortString2(self, order: str, s: str) -> str:
        dic = {}
        for idx, c in enumerate(order):
            dic[c] = idx

        sorted_s_array = sorted(s, key=lambda c: dic.get(c, 0)) # Takes O(n) space because a new sorted s array is created
        return ''.join(sorted_s_array)