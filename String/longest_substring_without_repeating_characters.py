# lc 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        l, r = 0, 0
        char_set = set()
        while r < n:
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len, r - l + 1) # 如果想象成dp array， 此时在计算的是以l为右边界的最长无重复substring
                r += 1
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])
                # 如果想象成dp array， 此时在计算的是以l为右边界的最长的substring
                # 为什么不需要下面这行代码呢，因为肯定不会是最长的，最多就是l和r重合，长度为1
                # 如果需要知道每个点作为右边界的最长无重复substring，那可以要这一行
                # max_len = max(max_len, r - l + 1) 
                r += 1

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))