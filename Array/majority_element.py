# lc 169
import math

class Solution:
    # 这题先决条件就是majority element一定存在

    # sc O(1)的解法
    # Moore Voting Algorithm
    # The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array, 
    # it will always remain in the lead, 
    # even after encountering other elements.
    # 假如有四个2，两个3，一个1
    # 2 2 2 2 3 3 1 为方便理解假如array恰好是sort的，只有在candidate = 2的情况下才可能有剩余，其他candidate剩余是不可能 > 0的
    def majority_element1(self, nums: list[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

    # 正常人第一反应肯定是dict记录数字出现的次数
    def majority_element2(self, nums: list[int]) -> int:
        n = len(nums)
        limit = math.floor(n / 2)
        num_to_freq = {}

        max_freq = 1
        maj_element = nums[0]
        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 1
            else:
                num_to_freq[num] += 1
                if num_to_freq[num] > limit:
                    return num
                if num_to_freq[num] > max_freq:
                    max_freq = num_to_freq[num]
                    maj_element = num

        return maj_element
    
a = Solution()
print(a.majority_element1([3,2,3]))