# lc 60
class Solution:
    # brute force worst case O(n*n!), space O(n) length of the tree
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        for i in range(n):
            nums.append(i + 1)

        visited = set()
        path = list()
        self.permutation_wanted = []
        self.counter = 0

        def permute_helper():
            if len(self.permutation_wanted) != 0:
                return

            if len(path) == n:
                if self.counter < k - 1:
                    self.counter += 1
                else:
                    self.permutation_wanted = list(path)
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

        str_arr = [str(e) for e in self.permutation_wanted]
        return "".join(str_arr)

s = Solution()
print(s.getPermutation(3, 3))