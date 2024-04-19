# lc 162
class Solution:
    # Time - O(logn) n = len(nums), space O(1)
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            right_nb = nums[mid + 1] if mid < len(nums) - 1 else -float('inf')
            left_nb = nums[mid - 1] if mid > 0 else -float('inf')
            if left_nb < nums[mid] > right_nb:
                return mid
            elif nums[mid] > right_nb: # 这意味着left_nb大于nums[mid]
                r = mid - 1
            else: # 意味着right_nb大于nums[mid]
                l = mid + 1

        # Because Peak exists, the above code will catch any peak
        # even if it might be the leftmost or rightmost element.
        return -1

s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))