# lc 704
from math import floor
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # 这是我随便试的代码，看到lc981之后试的例子，虽然可以ac lc704，但一般不这样写逼进的方法，在找out of range的数
        # 比如比最右大或者最左小，或者是找第一个目标或者最后一个目标时，用逼进的方法最好
        while l <= r:
            mid = floor((l + r) / 2)
            if nums[mid] <= target: # 这意味着从左边逼近目标，如果目标比最大（右）还打，那最接近的就是最后的nums[r]
                l = mid + 1
            else: # nums[mid] > target # 同理如果等号在这 nums[mid] >= target，就是从右边逼近目标，如果目标比最左还小，那最接近目标的就是nums[l]
                r = mid - 1
        print(f'l: {l}')
        print(f'r: {r}')
        
        # 切记，如果在mid 和target比较中加了等号，意味着在从左（右）逼近，那出来之后一定要判断是不是out of range
        return r if r >= 0 and nums[r] == target else -1

s = Solution()
print(s.search([0,1,9,9,9,9,9,9], 9)) # lc981 例子，假如timestamp target 是10，那应该返回9，此时l会一直前移，因为所有元素都小于10，直到l移出范围，此时应该返回的是r
