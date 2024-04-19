# lc 249
class Solution:
    # T: O(m*n) n - length of strings, m - max size of the string in strings
    # S: O(m*n)
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        key_to_strings = {}
        for s in strings:
            key = ''
            for i in range(len(s) - 1):
                diff = ord(s[i + 1]) - ord(s[i])
                key += f'{(diff % 26)},'
            if key not in key_to_strings:
                key_to_strings[key] = []
            key_to_strings[key].append(s)
        
        return list(key_to_strings.values())

s = Solution()
print(s.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))