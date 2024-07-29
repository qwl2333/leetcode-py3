# lc 704
from math import floor
class Solution:
    # 找 upper bound
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # 这是我随便试的代码，看到lc981之后试的例子，虽然可以ac lc704，但一般不这样写逼进的方法，在找out of range的数
        # 比如比最右大或者最左小，或者是找第一个目标或者最后一个目标时，用逼进的方法最好
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target: # 这意味着从左边逼近目标，如果目标比最大（右）还大，那最接近的就是最后的nums[r]
                l = mid + 1
            else: # nums[mid] > target # 同理如果等号在这 nums[mid] >= target，就是从右边逼近目标，如果目标比最左还小，那最接近目标的就是nums[l]
                r = mid - 1
        print(f'l: {l}')
        print(f'r: {r}')
        
        # 切记，如果在mid 和target比较中加了等号，意味着在从左（右）逼近，那出来之后一定要判断是不是out of range
        return r if r >= 0 and nums[r] == target else -1
    
    # lower bound and upper bound, 意思是可以插入的lowest and highest position where the target could be inserted without breaking the order
    # sorted array 1,2,3,3,4,5 插入 3, lower bound是第一个>=3也就是第一个3（index 2），upper bound是第一个>3的数4（index 4）
    # lower bound可以用来找第一个大于等于target，也可以用来找最后一个严格小于target，因为第一个大于等于target的前面一个就是<target的
    # upper bound可以用来找第一个严格大于target，也可以用来找最后一个<=target的，因为第一个严格大于target的前一个就是最后一个<=target的

    # 以下这个是用lower bound找第一个可以>=target的位置
    def lower_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else: # nums[mid] < target
                l = mid + 1
        
        return l # l-1=r 就是最后一个<target的位置，注意r有可能out of range 如果l是第一个元素, l是第一个>=target的位置

    # 以下这个数upper bound找第一个可以>target的位置
    def upper_bound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            else: # nums[mid] <= target
                l = mid + 1
        
        return l # l-1=r 其实就是最后一个<=target的位置, l是第一个>target的位置, 
                 # 注意l可能out of range, 例如target = 7, nums=[2,3,4,5] r = 3, l = 4
                 # 注意r也可能out of range，例如target = 1, nums=[2,3,4,5] r = -1, l = 0

s = Solution()
print(s.upper_bound([9,9,9,9,9,9], 9)) # lc981 例子，假如timestamp target 是10，那应该返回9，此时l会一直前移，因为所有元素都小于10，直到l移出范围，此时应该返回的是r
