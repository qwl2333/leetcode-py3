# lc 88
class Solution:
    # 两个sorted array， 一个m + n长度，有m个sorted elements，另一个n长度有n个sorted elements
    # 合并成到第一个array里面让所有elements sorted
    # sol： 从后往前放
    # Time O(m + n), Space O(1)
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, i3 = m - 1, n - 1, m + n - 1

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i3] = nums1[i1]
                i3 -= 1
                i1 -= 1
            else:
                nums1[i3] = nums2[i2]
                i3 -= 1
                i2 -= 1
        while i2 >= 0:
            nums1[i3] = nums2[i2]
            i3 -= 1
            i2 -= 1

        return nums1

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))