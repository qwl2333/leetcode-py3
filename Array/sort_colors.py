# lc 75

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
        pivot_index = start # 当i经过的值比pivot_val小时，需要和pivot_index所在位置进行swap，所以pivot_index就是下一个可以进行swap的位置
        '''
        比如1,8,9,3,4',4  此时最后一个4是pivot value
        那么i经过1时, 此时pivot idx和i处在同一个位置, swap完之后不变, pivot index前进一步, i前进一步
           i经过8时, 此时pivot idx不动, 只移动i, 因为8>4, 8是一个需要之后被swap的位置, 什么时候swap, 直到下一个<4的出现, 进行swap
           i经过9时, 此时pivot idx还在8的位置, 9>4, 仍然不同pivot idx只动i
           i经过3时, 此时pivot idx还在8的位置, 3<4, 为了partition后所有小于4的都在左边, 
             此时需要和pivot idx也就是8 swap, 此时array是1,3,9,8,4,4, pivot idx移动一位到9, i移动一位
           i经过4'时, 4'并不是小于4的数, 所以partition的时候不用移动到左边,此时pivot idx在9
        移动到4'时循环结束了
        最后做一次swap, 此时array是 1,3,9,8,4',4 , 把pivot value 4和pivot idx 9 swap, 就可以得到partition后的结果
        1,3,4,8,4',9
        '''
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
                ct2 += 1

        for i in range(len(nums)):
            if ct0 != 0:
                nums[i] = 0
                ct0 -= 1
            elif ct1 != 0:
                nums[i] = 1
                ct1 -= 1
            else:
                nums[i] = 2
                ct2 -= 1
    
    # one pass 用双指针
    # Dutch National Flag algorithm: sorting an array containing three distinct values
    # 可以看neetcode
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
