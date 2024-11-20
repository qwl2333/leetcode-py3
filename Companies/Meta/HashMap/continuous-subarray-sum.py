# lc 523
# 和 lc 974 Subarray Sums Divisible by K 类似
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        pfx_sum_map = {} # prefix_sum % k -> idx
        pfx_sum = 0
        pfx_sum_map[0] = -1
        for idx, num in enumerate(nums):
            pfx_sum += num
            pfx_sum %= k
            if pfx_sum not in pfx_sum_map: # 一个pfx_sum的位置更新一次就可以了,因为只求是不是存在,不是求个数
                pfx_sum_map[pfx_sum] = idx
            elif idx - pfx_sum_map[pfx_sum] > 1: # pfx_sum already exists in pfx_sum_map and the length of sub array >= 2
                return True
        
        return False