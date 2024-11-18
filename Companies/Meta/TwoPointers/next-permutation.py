# lc 31 和 lc 670区分
class Solution:
    # 题目意思就是用nums的数随意排列，找下一个比nums大但是离nums最近的数
    # 一般情况[1,2,3] -> [1,3,2]
    # 例外是[3,2,1] -> [1,2,3]
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        从右往左边找到第一个k, nums[k] < nums[k + 1], 这样从[k+1:]到结尾都是descending的sequence,那这个数字一定是最大的
        比如3',4',4,3, k=0, 4',4,3一定是最大的那个permutation
        然后4',4,3 从右往左 找第一个比3'大的数, 和3'交换, 然后得到4,4',3',3, 再把[k+1:]的array reverse一下得到 4,3,3',4'就是我们要的答案
        """

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]: # go thru rightmost descending sequence
            i -= 1
        if i == 0:
            nums.reverse()
            return # all descending
        
        k = i - 1 # k is the position before rightmost descending sequence
        j = len(nums) - 1 # j is to find the first element in right side that > nums[k]
        while nums[j] <= nums[k]:
            j -= 1
        nums[j], nums[k] = nums[k], nums[j]

        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    # 二分找右边第一个 > nums[k]的
    def nextPermutationBinarySearchSol(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]: # go thru rightmost descending sequence
            i -= 1
        if i == 0:
            nums.reverse()
            return # all descending
        
        k = i - 1 # k is the position before rightmost descending sequence
        target = nums[k]
        j = self.binary_search(nums, k + 1, len(nums) - 1, target) - 1 # j is to find the first element in right side that > nums[k]
        nums[j], nums[k] = nums[k], nums[j]

        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    
    '''
     nums[k+1:] 是 reverse sorted array, 找第一个> target的位置
    '''
    def binary_search(self, nums, start, end, target): # find first > target
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
        return end # 这种情况是一定有解的,必存在>target的,所以不用点心out of bound

    '''
        也可以先找到位置k, k之后都是不严格递减的数列, 当nums[k] < nums[k + 1]
        然后reverse nums[k+1:], reverse之后k+1开始都是非严格地震局的数列
        然后k+1开始,找第一个>num[k]的, 和k的数swap
        这个和之前做法就是先reverse再找要swap的,可以避免不熟悉的逆序数组的二分
    '''


    def nextPermutation2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return

        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        k = i - 1
        target = nums[k]
        j = self.binary_search2(nums, i, len(nums) - 1, target)
        nums[j], nums[k] = nums[k], nums[j]

    '''
        因为nums[k+1:] 已经sorted过了
        所以此时是在sorted 的nums[k+1:]里找第一个>target的位置
    '''
    def binary_search2(self, nums, start, end, target): # find first > target
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        return start

s = Solution()
nums = [9,8,7,6]
s.nextPermutation(nums)
print(nums)