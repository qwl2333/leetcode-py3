# lc 424
# neetcode https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    # Time O(26n), Space O(26), 
    # 双指针，l r组成的substring的长度 - l,r之间最高freq出现的字母 <= k, 这个substring才符合要求,
    # 什么意思呢，加入window之间最高频率的字母是a, 剩下的字母一共也不到k个,那就可以完成替换,然所有在window内
    # 的字母都是a
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        l, r = 0, 0
        max_len = 0
        while r < n:
            freq[s[r]] = freq.get(s[r], 0) + 1
            while (r - l + 1) - max(freq.values()) > k: # max(freq.values()) is O(26) since 26 upppercase letters
                                                        # 这里意味着window内除最高频率字母外的其他字母太多>k个
                                                        # 必须移动左边, 为啥移动左边不是右边
                                                        # 移动右边也改不了,里面其他字母个数超过了k
                                                        # 移动左边有可能会把其他字母去掉
                freq[s[l]] -= 1
                l += 1
            # 此时除了最高频率字母, 其他字母的个数是一定小于等于k的, 是符合要求的substring, 可以计算长度
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len