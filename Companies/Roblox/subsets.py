# lc 78
class Solution:
    # Time O(2^n)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        path = []
        res = []
        def dfs_helper(i: int):
            if i == n:
                res.append(list(path))
                return
            
            res.append(list(path))
            for i in range(i, n):
                path.append(nums[i])
                dfs_helper(i + 1)
                path.pop()
        
        dfs_helper(0)
        return res
    '''
    leetcode似乎不是原题：
    给定一个正整数组，返回其全部subset sum，
    比如[1,3,5] -> [0,1,3,4,5,6,8,9]；
    进阶版本是不允许subset有相邻元素的话，还是返回全部可能的sum，比如[1,3,5] -> [0,1,3,5,6]。

    1) sums = [sum(sublist) for sublist in list_of_lists]

    2) dfs_helper(i + 2)

    '''
    def subsets_no_neighbor(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        path = []
        res = []
        def dfs_helper(i: int):
            if i == n:
                res.append(list(path))
                return
            
            res.append(list(path))
            for i in range(i, n):
                path.append(nums[i])
                dfs_helper(i + 2)
                path.pop()
        
        dfs_helper(0)
        return res

s = Solution()
print(s.subsets_no_neighbor([1,3,5]))