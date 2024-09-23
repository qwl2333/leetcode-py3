# lc 215
from heapq import heappop, heappush
class Solution:
    # 第一种是priority queue, time O(nlogk), space O(k) min_q max needs k
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_q = []
        for num in nums:
            heappush(min_q, num)
            if len(min_q) > k:
                heappop(min_q)
        
        return min_q[0]

    # 第二种是quick select time avg O(n) wst O(n^2)   
    # space 考虑栈内存wst case O(n), avg O(logn), 不考虑应该是O(1)
    # 假设每次partition取得值都是median，那每次partition都可以去掉一半的数组，所以加起来 N（1 + 1/2 + 1/4 + 1/8 ...） = 2N， 
    # 所以是O（n）理想状态下，实际是O（n） to O（n^2）worst case: pivot chosen is always the the largest element
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        # partion完成之后保证pivot index左边都小于pivot value
        def partition(left: int, right: int, nums: list[int]) -> int:
            pivot_value = nums[right]
            for r in range(left, right):
                if nums[r] < pivot_value:
                    nums[r], nums[left] = nums[left], nums[r]
                    left += 1
            
            nums[left], nums[right] = nums[right], nums[left]
            return left # 返回pivot_index
        
        def quick_sort(nums: list[int], start: int, end: int):
            if start > end:
                return
            pivot_index = partition(start, end, nums)
            quick_sort(nums, start, pivot_index - 1)
            quick_sort(nums, pivot_index + 1, end)

        # 无序list里面, quck select, 选取的是从小到大sorted的list的index=k的数，
        # 因为index is 0 based. 所以不是第k小的数, 应该是第k+1小的数
        # 所以如果是选第k大的，实际上是选index = len(nums) -k 小的数
        def quick_select(nums: list[int], start: int, end: int, k: int):
            if start > end:
                return
            pivot_index = partition(start, end, nums)
            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                return quick_select(nums, pivot_index + 1, end, k)
            else:
                return quick_select(nums, start, pivot_index - 1, k)
    
        return quick_select(nums, 0, len(nums) - 1, len(nums) - k) # quick select是选择sorted 后从小到大 index = len(nums) - k
                                                                   # 比如 [1,2,3,4,5] len = 5, k = 2
                                                                   # 找第二大的4, 就是找第四小的4, index就是3 = 5 - 2
