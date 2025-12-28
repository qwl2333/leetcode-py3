# lc 249
class Solution:
    # T: O(m*n) n - length of strings, m - max size of the string in strings
    # S: O(m*n)
    '''
    在 Python 中：-1 % 26 = 25
    在 C# / Java / C++ 中：-1 % 26 = -1
    在 C# 中获得正数余数的通用公式
    int result = ((a % n) + n) % n;

    // 例子：
    // ((-1 % 26) + 26) % 26 
    // = (-1 + 26) % 26 
    // = 25 % 26 = 25
    '''
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        key_to_strings = {}
        for s in strings:
            key = ''
            for i in range(len(s) - 1):
                diff = ord(s[i + 1]) - ord(s[i])
                '''
                 python 不同于c# 特有的
                 ba: -1 % 26 = 25
                 az: 25 % 26 = 25
                 为了通用一点也可以
                    ((diff % 26) + 26) % 26 instead of (diff % 26)
                '''
                key += f'{(diff % 26)},' 
            if key not in key_to_strings:
                key_to_strings[key] = []
            key_to_strings[key].append(s)
        
        return list(key_to_strings.values())

s = Solution()
print(s.groupStrings(["acb","bcd","acef","xyz","az","ba","a","z"]))