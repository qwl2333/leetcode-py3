# lc 215
from queue import PriorityQueue
class Solution:
    # 找第k大的数，用min heapq
    # time O(nlogk) space O(k)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = PriorityQueue()

        for num in nums:
            pq.put(num)
            if pq.qsize() > k:
                pq.get()

        return pq.queue[0]

    # quick select avg time O(n), worst case O(n^2), space O(1) 其实是logn的stack空间，但一般认为是常数空间
    # 原题找的是第k大的数，就是从大到小第k大
    # quick select是从小到大第k小的元素，所以要注意选的是第(len(nums) - k + 1)小，也就第k大的元素
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k) # 第(len(nums) - k + 1)小 对应的index是len(nums) - k

    '''
    Iterative way for quick select
    面试的时候用iterative的quick select, 因为空间复杂度为O(1)
    def quick_select(nums: list[int], start: int, end: int, k: int) -> int:
        while start <= end:   
            pivot_idx = partition(nums, start, end)
            if pivot_idx == k:
                return nums[pivot_idx]
            elif pivot_idx > k:
                end = pivot_idx - 1
            else:
                start = pivot_idx + 1
        
        return 10001
    ''' 

    def quick_select(self, nums: list[int], start: int, end: int, k: int):
        if start > end:
            return 10001
        
        pivot_idx = self.partition(nums, start, end)
        if pivot_idx == k:
            return nums[pivot_idx]
        elif pivot_idx > k:
            return self.quick_select(nums, start, pivot_idx - 1, k)
        else:
            return self.quick_select(nums, pivot_idx + 1, end, k)
    
    # partion完成之后保证pivot index左边都小于pivot value
    def partition(self, nums: list[int], start: int, end: int):
        pivot_value = nums[end]
        pivot_idx = start
        for i in range(start, end):
            if nums[i] < pivot_value:
                nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                pivot_idx += 1
        nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
        return pivot_idx