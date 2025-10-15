# lc 215
from queue import PriorityQueue
from heapq import heappush, heappop
class Solution:

    # quick select time O(n) wst case O(n^2), space O(1)
    # 注意选第k大和第k小，partition，和快选的写法是不同的
    # 选第k大的element
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            pvt = self.partition(nums, l, r)
            if pvt == k - 1: # 这里是k-1，因为第k大的index其实是k-1
                return nums[pvt]
            elif pvt > k - 1:
                r = pvt - 1
            else:
                l = pvt + 1
        return 10001
    
    def partition(self, nums: list[int], l: int, r: int) -> int:
        pivot_idx = l
        pivot_value = nums[r]
        for i in range(l, r): # i的范围是[l, r - 1]，因为一般选最右为pivot
            if nums[i] > pivot_value: # 注意这里的符号 如果是> : pivot_idx 左边都 > pivot_value， 如果是 < : pivot_idx 左边都 < pivot_value
                nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                pivot_idx += 1
        
        nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
        return pivot_idx

    """
    Iterative way for quick select
    面试的时候用iterative的quick select, 因为空间复杂度为O(1)
    """
    def quick_select_k_smallest(self, nums: list[int], start: int, end: int, k: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            pivot_idx = self.partition2(nums, start, end)
            if pivot_idx == k - 1:
                return nums[pivot_idx]
            elif pivot_idx > k - 1:
                end = pivot_idx - 1
            else:
                start = pivot_idx + 1
        
        return 10001

    # partion完成之后保证pivot index左边都小于pivot value
    # 考虑两个例子
    # [1,2,3,4]     pivot_idx 会走到end的位置， 最后一次交换其实就是同一个元素的交换
    # [9,8,1,2,3,4] -> [1,8,9,2,3,4] -> [1,2,9,8,3,4] -> [1,2,3,8,9,4] -> [1,2,3,4,9,8]
    def partition2(self, nums: list[int], start: int, end: int):
        pivot_value = nums[end]
        pivot_idx = start
        for i in range(start, end): # start -> end -1
            if nums[i] < pivot_value:
                nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                pivot_idx += 1
        nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
        return pivot_idx

    # 找第k大的数，把小的排出去，就剩k个大的，用min heapq，如果是找第k小的数，把大的排出去，就剩k个小的，用max_heap
    # time O(nlogk) space O(k)
    def findKthLargestMinHeap(self, nums: list[int], k: int) -> int:
        # pq = PriorityQueue()

        # for num in nums:
        #     pq.put(num)
        #     if pq.qsize() > k:
        #         pq.get()

        # return pq.queue[0]
        min_heap = []

        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        
        return min_heap[0]

###### 看到上面就行，三种解法了解，min_heap, k_smallest, k_largest

    def quick_select(self, nums: list[int], start: int, end: int, k: int):
        if start > end:
            return 10001
        
        pivot_idx = self.partition2(nums, start, end)
        if pivot_idx == k:
            return nums[pivot_idx]
        elif pivot_idx > k:
            return self.quick_select(nums, start, pivot_idx - 1, k)
        else:
            return self.quick_select(nums, pivot_idx + 1, end, k)