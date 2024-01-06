# lc 238

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        size = len(nums)
        prefix_product = [1] * size
        suffix_product = [1] * size
        result = [1] * size

        for i in range(1, size):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        for i in range(size - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        for i in range(0, size):
            result[i] = prefix_product[i] * suffix_product[i]
        
        return result
    
a = Solution()
print(a.product_except_self([-1,1,0,-3,3]))
