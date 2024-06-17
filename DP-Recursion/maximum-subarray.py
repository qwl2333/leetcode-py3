# lc 53
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            max_sum = max(max_sum, dp[i])
        return max_sum