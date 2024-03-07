# lc 153
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        if l < n:
            return nums[l]
        else:
            return nums[0]

s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))
