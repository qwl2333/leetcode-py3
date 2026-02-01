# lc 724
class Solution:
    """
    核心数学推导：
    1. 设数组总和为 total_sum
    2. 对于索引 i, 其左侧元素之和为 left_sum
    3. 则其右侧元素之和为 right_sum = total_sum - left_sum - nums[i]
    4. 支点条件: left_sum == right_sum
    5. 代入等式: left_sum = total_sum - left_sum - nums[i]
    6. 整理得最终公式: 2 * left_sum + nums[i] == total_sum
    cornor case:
        nums=[0], 因为左右侧都是0, 所以返回index 0, 所以这个cornor case也成立
    """
    def pivotIndex(self, nums: list[int]) -> int:
        # 1. 健壮性检查 (虽然题目约束 1 <= nums.length)
        if not nums:
            return -1
        
        # 2. 先求出全队的总和
        total_sum = sum(nums)
        
        # 3. 维护一个运行中的左侧和
        prefix_sum = 0
        
        # 4. 遍历每个潜在的“支点”
        for i, x in enumerate(nums):
            # 套用公式：2 * 左侧和 + 当前值 == 总和
            if 2 * prefix_sum + x == total_sum:
                return i
            
            # 如果不是支点，就把当前值加到左侧和里，继续往后看
            left_sum += x
            
        return -1