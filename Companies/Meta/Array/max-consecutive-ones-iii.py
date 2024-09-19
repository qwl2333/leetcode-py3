# lc 1004 类似 lc 424 longest repeating character replacement
class Solution:
    # Time O(n) Space O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        used_flip = 0
        max_len = 0
        while r < n:
            if nums[r] == 0:
                used_flip += 1
            
            while used_flip > k:
                if nums[l] == 0:
                    used_flip -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len