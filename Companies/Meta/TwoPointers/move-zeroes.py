# lc 283
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                r += 1
                continue
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r += 1
        return nums