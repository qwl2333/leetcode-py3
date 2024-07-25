# lc 39
# https://leetcode.com/problems/combination-sum/solutions/742449/explanation-of-time-complexity/
# Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
# Space complexity: O(M/min_cand)

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        n = len(candidates)
        combination = []
        result = []

        def find_combination_sum_helper(remain: int, start_idx: int, path: list[int]) -> None:
            if remain == 0:
                result.append(list(path))
                return

            for i in range(start_idx, n):
                if candidates[i] > remain:
                    return

                path.append(candidates[i])
                find_combination_sum_helper(remain - candidates[i], i, path)
                path.pop()

        find_combination_sum_helper(target, 0, combination)
        return result

a = Solution()
print(a.combinationSum([2,3,6,7], 7))
