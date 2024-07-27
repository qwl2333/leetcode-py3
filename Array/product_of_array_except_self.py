# lc 238

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        prefix_product = [1 for _ in range(size + 1)]
        suffix_product = [1 for _ in range(size + 1)]
        result = [1 for _ in range(size)]

        for i in range(1, size + 1):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        for i in range(size - 1, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]

        for i in range(0, size):
            result[i] = prefix_product[i] * suffix_product[i + 1]
        
        return result
    
a = Solution()
print(a.productExceptSelf([-1,1,0,-3,3]))
