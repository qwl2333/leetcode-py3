class Solution:
    # Time O(n), space O(1)
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0
        
        # p1,p2 同时往右走，直到任何一方结束
        # 如果是valid的abbreviation，p1,p2应该都结束了遍历
        # 如果有没有遍历完的，证明两个字符串长度不同
        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2].isdigit():
                if abbr[p2] == '0':
                    return False
                count = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    count = 10 * count + int(abbr[p2])
                    p2 += 1
                p1 += count
            else:
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1
        
        return p1 == len(word) and p2 == len(abbr)

s = Solution()
print(s.validWordAbbreviation('substitution', 'sub4u4'))