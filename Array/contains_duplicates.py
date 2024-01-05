# lc 217

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        
        return False
    
a = Solution()
print(a.contains_duplicate([7, 1 , 5 , 3 , 3, 6, 4]))