# Given a string S of N characters, returns the length of the longest string that’s both a proper prefix and suffix of S. Proper means the string is shorter than S
# for instance, s = ‘abbabba’, returns 4 because ‘abba’ is the proper prefix and suffix
# s = ‘codility, returns 0 because ‘’ is the proper prefix and suffix

class Solution:
    # Time: O(n^2) Space: O(n^2)
    def find_longest_proper_identical_prefix_suffix(self, s: str) -> int:
        n = len(s)
        l, r = 0, n
        longest_proper = 0
        while l < n and r >= 1:
            print(f'l:{l}, r:{r}')
            prefix_s = s[0:l]
            suffix_s = s[r:n]
            print(f'pfx: {prefix_s}')
            print(f'sfx: {suffix_s}')
            if prefix_s == suffix_s:
                longest_proper = max(longest_proper, l)
            l += 1
            r -= 1
        return longest_proper
    
    # https://www.youtube.com/watch?v=3IFxpozBs2I&t=802s&ab_channel=%E9%BB%84%E6%B5%A9%E6%9D%B0
    # https://www.geeksforgeeks.org/longest-prefix-also-suffix/
    # KMP alg need Longest common Prefix Suffix array
    # Function to compute LPS array O(n)
    def computeLPSArray(self, pat: str) -> list[int]:
        length = 0  # length of the previous longest prefix suffix

        m = len(pat)
        lps = [0 for i in range(m)] # lps[0] is always 0
        i = 1
    
        # the loop calculates lps[i] for i = 1 to m-1
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar
                # to search step.
                if length != 0:
                    length = lps[length-1]                              # 找到之前最长prefix里面的最长prefix是多少，从而判断最后加进来的那个字符可能组成为多长的新的prefix, 在这个视频的例子里面就是找ABA的最长prefix，就是A, 然后就要判断最新的那个字符里面是不是B，在这里并不是，所以要再往回退一部，只看第一个字符和最后一个字符是不是相同。如果是“aaabaaaa”的话，那在最后一个字符判断prefix的时候，len = 3, 所以同样看"aaa"的最大prefix，是“aa”, 然后 len 此时变为2，所以只要判断最后那个字符是不是“a”，如果是的话，那len++之后，最长prefix长度就又是3了。
                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1
        
        return lps

s = Solution()
print(s.computeLPSArray('aaabaaaa'))

