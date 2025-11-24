# lc 34

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first_bigger_or_equal_to(nums: list[int], l: int, r: int, target: int) -> int:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            if l == len(nums):
                return -1
            return l
        
        def find_last_smaller_or_equal_to(nums: list[int], l: int, r: int, target: int) -> int:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            if r == -1:
                return -1
            return r
    
        n = len(nums)
        f = find_first_bigger_or_equal_to(nums, 0, n - 1, target)
        l = find_last_smaller_or_equal_to(nums, 0, n - 1, target)
        if f != -1 and l != -1 and nums[f] == target and nums[l] == target:
            return [f, l]
        else:
            return [-1, -1]