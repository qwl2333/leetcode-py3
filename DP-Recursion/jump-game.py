# lc 55
class Solution:
    # t O(n) s O(1)
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        rightmost = 0
        for idx, num in enumerate(nums):
            if idx <= rightmost:
                rightmost = max(idx + num, rightmost)
            else:
                return False
        
        return True if rightmost >= n - 1 else False