# lc 1539 类似 lc 1060
# https://leetcode.com/problems/kth-missing-positive-number/solutions/779999/java-c-python-o-logn/
# 看第一个评论by ryz
'''
After while loop is stopped, l - 1 is our target index because, 
B[l - 1] represents how many positive is missing at index l - 1 that number must be smaller than K, since we are finding first element in B >= K 
so result is A[l -1](the largest number in A that is less than result) + K - B[l - 1](offset, how far from result) = (A[l - 1]) + (k - (A[l - 1] - l)) = l + k
'''
class Solution:
    # time: O(logn)
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # 计算到 arr[mid] 为止，前面缺失了多少个正整数。
            # 公式: 实际值 - 理想值 = arr[mid] - (mid + 1)
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count >= k:
                # 缺失数量足够或超出了 k。
                # 答案在 mid 的左边或就是 mid。向左收缩右边界 r。
                r = mid - 1
            else:
                # 缺失数量不足 k。
                # 答案在 mid 的右边。向右推进左边界 l。
                l = mid + 1
        
        # ----------------------------------------------------
        # **循环结束时 l 和 r 的含义：**
        # r (Right): 最后一个 '缺失数量不足 k' 的索引。 (arr[r] 之前的缺失数 < k)
        # l (Left):  第一个 '缺失数量达到或超过 k' 的索引。 (arr[l] 之前的缺失数 >= k)
        # ----------------------------------------------------
        
        # 我们基于 r (最后一个不满足条件的索引) 来计算结果。

        # 步骤 1: 确定到 arr[r] 之前，已经缺失了多少个数字 (Missing_r)。
        # 需要处理 r = -1 的情况，此时 arr[r] 无法访问。
        if r < 0:
            # 如果 r = -1，说明第 k 个缺失数字在 arr[0] 之前。 比如 [6], k = 5
            missing_count_r = 0 
        else:
            # 缺失数量 = arr[r] - (r + 1)
            missing_count_r = arr[r] - (r + 1)

        # 步骤 2: 计算我们还需要往后数多少个数字 (Need)
        # Need = k - 截止到 arr[r] 已经缺失的数量
        needed_jump = k - missing_count_r

        # 步骤 3: 确定最终结果 (Result)
        if r < 0:
            # 结果在 arr[0] 之前，答案就是 k (即 0 + k)。
            result = k
        else:
            # 结果 = 最后一个实际数 (arr[r]) + 需要跳过的数 (needed_jump)
            result = arr[r] + needed_jump

        return result

# 注意：如果将 result = arr[r] + needed_jump 进行代数化简，结果始终等于 r + 1 + k。
# 但为了清晰展示步骤，我们保留了中间变量。
s = Solution()
print(s.findKthPositive([2,3,4,7,11], 5))
