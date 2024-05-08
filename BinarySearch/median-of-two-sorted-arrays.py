# lc 4
class Solution:
    # time O(log(min(n,m)))
    # space O(1)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len1
        while left <= right: # left right stands for lower and higher bound of the cut in nums1, from 0 to len1
            cut_1 = (left + right) // 2
            cut_2 = (len1 + len2 + 1) // 2 - cut_1 # 这个(len1 + len2 + 1)能保证当len1 + len2是奇数时，cut完之后，median那个点必在左边的l1,l2中
            l1 = nums1[cut_1 - 1] if cut_1 - 1 >= 0 else -float('inf')
            r1 = nums1[cut_1] if cut_1 < len1 else float('inf')
            l2 = nums2[cut_2 - 1] if cut_2 - 1 >= 0 else -float('inf')
            r2 = nums2[cut_2] if cut_2 < len2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (len1 + len2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l2 > r1: # l2 > r1 means l2 in nums2 is too big, need to make it smaller by making cut_1 bigger
                left = cut_1 + 1
            else: # l1 > r2
                right = cut_1 - 1
    
        return -1