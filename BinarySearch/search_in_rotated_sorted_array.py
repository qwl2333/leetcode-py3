# lc 33
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] > target or nums[mid] < nums[0]:
                    r = mid - 1
                else: # nums[mid] < target and nums[mid] >= nums[0]
                    l = mid + 1
            else:
                if nums[mid] >= nums[0] or nums[mid] < target:
                    l = mid + 1
                else: # nums[mid] > target and nums[mid] < nums[0]
                    r = mid - 1
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
        