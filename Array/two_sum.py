# lc 1

class Solution:
    # one iteration
    def two_sum1(self, nums: list[int], target: int) -> list[int]: # self refers to the instance of the class that the method is being called on. 
        num_to_index = {} # map from value to index of nums

        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement not in num_to_index:
                num_to_index[nums[i]] = i
            else:
                return [i, num_to_index[complement]] 
        
        return []
    
    # two iterations
    def two_sum2(self, nums: list[int], target: int) -> list[int]:
        value_to_index = {}

        n = len(nums)
        for i in range(n):           
            value_to_index[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in value_to_index and i != value_to_index[complement]: # i != value_to_index[complement] is to make sure it is not [3, 2, 4] target 6, we are not returning [0, 0]
                return [i, value_to_index[complement]]
        
        return []
    


a = Solution()
print(a.two_sum1([2, 7, 11, 15], 9))
