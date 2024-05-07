# lc 198
class Solution:
    # time O(n), space 0(n)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n - 1]

s = Solution()
print(s.rob([1,2,3,1]))