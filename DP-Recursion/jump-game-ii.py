# lc 45
# https://www.youtube.com/watch?v=XYJ6jIlCmio&ab_channel=FLAGeek%E5%AE%98%E6%96%B9%E9%A2%91%E9%81%93
class Solution:
    # t O(n) s O(1)
    def jump(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 0

        
        steps = 0
        left_boundary = 0
        right_boundary = 0
        for i in range(len(nums)):
            right_boundary = max(right_boundary, i + nums[i])

            if i == left_boundary:
                steps += 1
                left_boundary = right_boundary
                if right_boundary >= len(nums) - 1:
                    return steps
        
        return -1
