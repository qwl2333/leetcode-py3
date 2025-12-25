# lc 16 解法和15类似
class Solution:
    # TC O(N^2)  SC: O(1)
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # 1. 排序：这是双指针法的基础
        nums.sort()
        n = len(nums)
        # 初始化最接近的和为前三个数的和
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # 优化：简单的去重，如果当前数字和上一个一样，可以跳过以减少计算
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, n - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                # 如果当前和正好等于 target，直接返回，没有比这更接近的了
                if current_sum == target:
                    return current_sum
                
                # 更新最接近的和
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # 根据当前和与 target 的关系移动指针
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum