# lc 1060 类似 lc 1539
class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        # [4,7,9,10]
        # [4,5,6,7]
        # [0,2,3,3] find last element < k

        # [1,2,4]
        # [1,2,3]
        # [0,0,1]

        start = nums[0]
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] - (mid + start) < k: #     find last element < k, 操作的是l=mid+1 说明r才是last element < k
                l = mid + 1
            else: # nums[mid] - (mid + start) >= k  find first element >= k, 操作的是r=mid-1 说明l才是first elment >=k
                r = mid - 1
        
        print(nums[r])
        return k + r + start # nums[r] + k - (nums[r] - (r + start)) 简化之后