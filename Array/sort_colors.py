# lc 76

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)

    # quick sort, in place sorting, if considering stack memory it is O(logn), time O(nlogn)
    def quick_sort(self, nums: list[int], start: int, end: int) -> None:
        if start >= end:
            return
        pivot_index = self.partition(nums, start, end)
        self.quick_sort(nums, start, pivot_index - 1)
        self.quick_sort(nums, pivot_index + 1, end)
    
    def partition(self, nums: list[int], start: int, end: int) -> int:
        pivot_value = nums[end]
        pivot_index = start
        for i in range(start, end):
            if nums[i] < pivot_value:
                self.swap(nums, i, pivot_index)
                pivot_index += 1
        self.swap(nums, pivot_index, end)
        return pivot_index

    
    def swap(self, nums: list[int], i: int, j: int) -> None:
        if i == j:
            return
        
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    # counting sort
    def counting_sort(self, nums: list[int]) -> None:
        ct0 = 0
        ct1 = 0
        ct2 = 0
        for num in nums:
            if num == 0:
                ct0 += 1
            elif num == 1:
                ct1 += 1
            else:
                ct2 += 2

        for i in range(len(nums)):
            if ct0 != 0:
                nums[i] = 0
                ct0 -= 1
            elif ct1 != 0:
                nums[i] = 1
                ct1 -= 1
            else:
                nums[i] = 2
                ct2 -= 2
    
    # one pass 用双指针
    # Dutch National Flag algorithm: sorting an array containing three distinct values
    def one_pass_sort(self, nums: list[int]) -> None:
        n = len(nums)
        next_zero = 0
        i = 0
        next_two = n - 1
        while i <= next_two:
            if nums[i] == 0:
                nums[next_zero], nums[i] = nums[i], nums[next_zero]
                next_zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else: 
                nums[next_two], nums[i] = nums[i], nums[next_two]
                next_two -= 1
