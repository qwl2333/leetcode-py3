# lc 974
# 与 lc 523 Continuous Subarray Sum 类似
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        pfx_sum_map = {} # prefix_sum % k -> freq
        pfx_sum = 0
        pfx_sum_map[0] = 1
        count = 0
        for num in nums:
            pfx_sum += num
            pfx_sum %= k
            if pfx_sum < 0:
                pfx_sum += k
            if pfx_sum in pfx_sum_map:
                count += pfx_sum_map[pfx_sum]
                pfx_sum_map[pfx_sum] += 1
            else:
                pfx_sum_map[pfx_sum] = 1
        
        return count