# lc 46
class Solution:
    '''
    TC: O(n * n!) in total we have n! permutations, every permutation we need to iterate n element
    详细推导：
    time O(n * n!)
    N + N*(N-1) + N*(N-1)*(N-2) + ... + N!
    recursion tree一共n层, 第一层n个节点, 最后一层的叶子结点是n!个
    搜索树一共有 n!+n!2!+n!3!+…=n!(1+12!+13!+…)≤n!(1+12+14+18+…)=2n!n!+n!2!+n!3!+…=n!(1+12!+13!+…)≤n!(1+12+14+18+…)=2n! 个内部节点，
    在每个内部节点内均会for循环 n 次，因此内部节点的计算量也是 O(n*n!)。 
    所以总时间复杂度是 O(n*n!)。
    '''
    def permute(self, nums: list[int]) -> list[list[int]]:
        visited = set()
        path = list()
        n = len(nums)
        res = []

        def permute_helper():
            if len(path) == n:
                res.append(list(path))
                return

            for num in nums:
                if num in visited:
                    continue

                visited.add(num)
                path.append(num)
                permute_helper()
                visited.remove(num)
                path.pop()

        permute_helper()

        return res

s = Solution()
print(s.permute([1,2,3]))