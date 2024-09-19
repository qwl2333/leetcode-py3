# 1539
# https://leetcode.com/problems/kth-missing-positive-number/solutions/779999/java-c-python-o-logn/
# 看第一个评论by ryz
'''
After while loop is stopped, l - 1 is our target index because, 
B[l - 1] represents how many positive is missing at index l - 1 that number must be smaller than K, since we are finding first element in B >= K 
so result is A[l -1](the largest number in A that is less than result) + K - B[l - 1](offset, how far from result) = (A[l - 1]) + (k - (A[l - 1] - l)) = l + k
'''
class Solution:
    # time: O(logn)
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] - (mid + 1) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l + k # 看上面link里面ryz的结论,本质上是 (A[l - 1]) + (k - B[l - 1]), B[l] = A[l] - (l+1)
                     #                  比如在例子里面  7       + (5  -   3), 我在7,我左边有三个missing的, 我还差两个
s = Solution()
print(s.findKthPositive([2,3,4,7,11], 5))
