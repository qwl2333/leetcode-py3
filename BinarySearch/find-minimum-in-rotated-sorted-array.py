# lc 153
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]: # 相等的时候移动l, l就有可能out of range到n到位置,比如nums = 11,13,15,17, 
                                     # 至于为什么要移动l, 因为假如真的旋转过有两条线（意思是不考虑旋转n次导致array还是原来的array的情况），mid在0时, 最小的肯定还在右边，所以移动l继续在右边寻找
                l = mid + 1
            else:
                r = mid - 1
        if l < n:
            return nums[l]
        else:
            return nums[0]

s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))
