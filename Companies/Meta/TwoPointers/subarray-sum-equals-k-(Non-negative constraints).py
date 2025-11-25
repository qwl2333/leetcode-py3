'''
Given list of non-negative integers and an integer target, return whether a continuous sequence of input integers sums up to target.
// Test case 1
int[] numbers1 = {1, 2, 3, 4, 5};
int target1 = 9;
return true

// Test case 2
int[] numbers2 = {1, 3, 2, 5, 7, 2};
int target2 = 14;
return true

// Test case 3
int[] numbers3 = {4, 3, 2, 7, 1, 2};
int target3 = 10;
return true

// Test case 4
int[] numbers4 = {4, 3, 2, 7, 1, 2};
int target4 = 11;
return false

Solution: used sliding window apprach.
time - o(n)
space - o(1)
和lc 560类似,但是lc 560里面的数字可以是负数, 所以用prefix sum和hashmap更好,此题也可以用prefix sun + Hashmap, 但是space O(n)
双指针的解法和lc 1004类似
'''
class Solution:
    # t O(n) s O(1)
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        left, right = 0, 0
        current_sum = 0
        n = len(nums)
        
        while right < n:
            # 1. 进：先加上右边的数
            current_sum += nums[right]
            
            # 2. 缩：如果大了，左指针一直往右移
            while left <= right and current_sum > k: # left <= right 其实可要可不要,因为k>=0, 但current_sum=0是,还是会跳出循环
                                                     # left < right 的区别是 <= 可以保证current_sum变成0，<会让current_sum至少有一个数
                                                     # 在这题里面其实没啥区别，但是变种题 找到最短的子数组，其和>=k (LeetCode 209 变种) 就会有问题
                current_sum -= nums[left]
                left += 1
            
            # 3. 查：刚好等于 k
            if current_sum == k:
                return True
            
            # 4. 移：右指针手动前进一步
            right += 1
            
        return False