# Given two sorted arrays nums1 and nums2 of size m and n respectively and an int k. Find the k-th smallest element of these arrays.
# Note that it is the k-th smallest element in the sorted order, not the k-th distinct element.

# Example 1:

# Input: nums1 = [-2, -1, 3, 5, 6, 8], nums2 = [0, 1, 2, 5, 9], k = 4
# Output: 5
# Explanation: Union of above arrays will be [-2, -1, 0, 1, 2, 3, 5, 5, 6, 8, 9] and the 4th smallest element is 5.
# Example 2:

# Input: nums1 = [2, 4], nums2 = [6], k = 1
# Output: 6
# Explanation: union of above arrays will be [2, 4, 6] and the 1st smallest element is 6.
# You may assume k is always valid, 1 ≤ k ≤ m + n.

# Follow-up
# Can you do it in O(logk) time?
class Solution:
    # Time: O(log(min(n, m, k))) n,m is the length of num1 and nums2
    # Space: O(1)
    def find_kth_in_two_sorted_arrays(self, nums1: list[int], nums2: list[int], k: int) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.find_kth_in_two_sorted_arrays(nums2, nums1, k)
        
        left = max(k - len2, 0)
        right = min(k, len1)
        while left <= right: # left right stands for lower and higher bound of the cut in nums1, from 0 to len1
            cut_1 = (left + right) // 2
            cut_2 = k - cut_1
            l1 = nums1[cut_1 - 1] if cut_1 - 1 >= 0 else -float('inf')
            r1 = nums1[cut_1] if cut_1 < len1 else float('inf')
            l2 = nums2[cut_2 - 1] if cut_2 - 1 >= 0 else -float('inf')
            r2 = nums2[cut_2] if cut_2 < len2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l2 > r1: # l2 > r1 means l2 in nums2 is too big, need to make it smaller by making cut_1 bigger
                left = cut_1 + 1
            else: # l1 > r2
                right = cut_1 - 1
    
        return -1

    # Time O(logk), Space O(1) 尾递归，无额外的栈
    # 看不懂，以后再看
    # https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/8999/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # Make len1 always less than len2, 
        # so if there's an empty array, it's always len1.
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        
        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))

    
s = Solution()
print(s.find_kth_in_two_sorted_arrays([2,3,6,7,9],[1,4,8,10],1))
            




