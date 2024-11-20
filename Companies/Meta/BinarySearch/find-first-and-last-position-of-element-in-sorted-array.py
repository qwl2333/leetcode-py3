# lc 34

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        if not nums:
            return res

        def lower_bound(l: int, r: int) -> int: # first element >= target
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return l
        
        def upper_bound(l: int, r: int) -> int: # last element <= target
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return r
        n = len(nums)
        l = lower_bound(0, n - 1)
        if l == n or nums[l] != target:
            return res
        else:
            res[0] = l
        
        u = upper_bound(0, n - 1)

        if u < 0 or nums[u] != target:
            return res
        else:
            res[1] = u
        
        return res