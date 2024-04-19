# lc 2256
class Solution:
    # Time O(n), space O(n), 利用前缀和和后缀和，space也可以简化成O(1)
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = [0 for i in range(n + 1)]
        suffix_sum = [0 for i in range(n + 1)]
        for i in range(n):
            head = nums[i]
            tail = nums[n - 1 - i]
            prefix_sum[i + 1] = prefix_sum[i] + head
            suffix_sum[i + 1] = suffix_sum[i] + tail
        print(prefix_sum)
        print(suffix_sum)
        min_res = float('inf')
        res_res = -1
        for i in range(1, n):
            a = prefix_sum[i] // (i)
            b = suffix_sum[n - i] // (n - i)
            if min_res > abs(a - b):
                min_res = abs(a - b)
                res_res = i - 1
        
        c = prefix_sum[n] // n
        if c < min_res:
            return n - 1
        return res_res