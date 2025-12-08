# lc 26
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return -1
        l, r, n = 0, 0, len(nums)
        while r < n:
            if nums[l] == nums[r]:
                r += 1
            else: # nums[l] < nums[r]
                l += 1
                nums[l] = nums[r]
                r += 1
        
        return l + 1