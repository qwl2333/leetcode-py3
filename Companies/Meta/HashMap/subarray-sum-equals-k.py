#  lc 560
class Solution:
    # time O(n), space O(n)
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        prefix_sum_freq = {0 : 1}

        count = 0
        for i in range(n):
            prefix_sum += nums[i] # 1,2,3
            target = prefix_sum - k
            if target in prefix_sum_freq:
                count += prefix_sum_freq[target]
            prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1 # 这个一定要最后更新
                                                           # 因为我们在计算到目前i为止
                                                           # 有多少个subarray sum = k
                                                           # 如果在12行就更新会把自己也算进去
        '''
            prefix_sum_freq, 但是 [0,0,0] k = 0的情况 就是错的
            prefix_sum += nums[i] # 1,2,3
            prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1
            target = prefix_sum - k
            if target in prefix_sum_freq:
                count += prefix_sum_freq[target]
        '''                                                  
                                                           
        
        return count

s = Solution()
print(s.subarraySum([0,0,0], 0))