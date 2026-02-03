# lc 18
class Solution:
    # 简答版本, 会有重复的答案, 看最下面的例子
    def four_sum_simple(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort() # 第一步永远是排序
        n = len(nums)
        res = []

        # 第一层：固定第一个数
        for i in range(n):
            # 第二层：固定第二个数
            for j in range(i + 1, n):
                # 剩下的：双指针找最后两个
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
    # 去重版本
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # 【去重 1】：如果这个数字和上一个一样，跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1, n - 2):
                # 【去重 2】：同理，固定第二个数也要去重
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # 下面就是你熟悉的 2Sum 双指针
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # 【去重 3】：找到答案后，也要跳过重复的左指针和右指针
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
    
s = Solution()
print(s.four_sum_simple([-2, -1, 0, 0, 0, 1, 2], 0)) 
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-2, 0, 0, 2], [-1, 0, 0, 1], [-1, 0, 0, 1]]
# 看见了吗, 三个0 所以导致出现了重复的选择
# 需要去重