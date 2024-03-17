#  lc 560
class Solution:
    # time O(n), space O(n)
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0 for i in range(n + 1)]
        freq = {}
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        count = 0
        for e in prefix_sum:
            target = e - k
            if target in freq:
                count += freq[target]
            freq[e] = freq.get(e, 0) + 1
        
        return count

s = Solution()
print(s.subarraySum([0,0,0], 0))