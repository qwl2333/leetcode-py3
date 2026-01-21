# lc 53
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
            max_sum = max(max_sum, dp[i])
        return max_sum

        # 再简化到不需要dp array
        # n = len(nums)
        # pre_sum = nums[0]
        # max_sum = nums[0]
        # for i in range(1, n):
        #     if pre_sum > 0:
        #         pre_sum = nums[i] + pre_sum
        #     else:
        #         pre_sum = nums[i]
        #     max_sum = max(max_sum, pre_sum)
        # return max_sum