# lc 215
from heapq import heappop, heappush
class Solution:
    # 第一种是priority queue, time O(nlogk)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_q = []
        for num in nums:
            heappush(min_q, num)
            if len(min_q) > k:
                heappop(min_q)
        
        return min_q[0]

    # 第二种是quick select time O(n) space O（1）
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        # partion完成之后保证pivot index左边都小于pivot value
        def partition(left: int, right: int, nums: list[int]) -> int:
            pivot_value = nums[right]
            for r in range(left, right + 1):
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
    
        # 无序list里面选第k大的数
        # quick select O(n)   space O（1）
        # 假设每次partition取得值都是median，那每次partition都可以去掉一半的数组，所以加起来 N（1 + 1/2 + 1/4 + 1/8 ...） = 2N， 所以是O（n）理想状态下，实际是O（n） to O（n^2）worst case: pivot chosen is always the the largest element
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
    
        return quick_select(nums, 0, len(nums) - 1, len(nums) - k)
