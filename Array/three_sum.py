# lc 15

class Solution:
    # tc O(n^2) sc O(n)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # 当前数和上一个一样，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 本质上是在[i+1，n-1]里面找两个数之和是target， 可以两个nested的for loop遍历所有可能O(n^2), 
            # 也可以sort nums, 然后只需要双指针l,r 从外往里找nums[l]+nums[r] = target
            target = -nums[i]

            l = i + 1 # 为什么是永远从当前位置后一个开始找，因为result不允许重复，
                      # 之前找过某个元素num1的如果能和当前的num[i]组成和为0的triplet，
                      # 那一定在之前num[i] = num1的时候就找到过了
            r = n - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    print(f'j: {l}, k: {r}')
                    result.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    # 找到target之后，移动左右index后，还是要看是不是重复的数
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return result

a = Solution()
print(a.threeSum([-2, -2, 0, 0, 2, 2]))