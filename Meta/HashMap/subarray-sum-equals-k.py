#  lc 560
class Solution:
    # time O(n), space O(n)
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        freq = {0 : 1}

        count = 0
        for i in range(n):
            prefix_sum += nums[i] # 1,2,3
            target = prefix_sum - k
            if target in freq:
                count += freq[target]
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        
        return count

s = Solution()
print(s.subarraySum([0,0,0], 0))