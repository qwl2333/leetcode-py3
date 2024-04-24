# lc 46
class Solution:
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