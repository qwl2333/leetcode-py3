# lc 39
# https://leetcode.com/problems/combination-sum/solutions/742449/explanation-of-time-complexity/
# Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
# Space complexity: O(M/min_cand)

class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        combination = []
        result = []
        self.find_combination_sum_helper(candidates, target, 0, combination, result)

        return result

    
    def find_combination_sum_helper(self, candidates: list[int], remaining: int, start: int, combination: list[int], result: list[list[int]]) -> None:
        n = len(candidates)
        if start >= n or remaining < candidates[start]:
            return
        
        for i in range(start, n):
            if candidates[i] == remaining:
                combination.append(candidates[i])
                result.append(list(combination))
                combination.pop()
                return

            # remaining > candidates[i]
            combination.append(candidates[i])
            self.find_combination_sum_helper(candidates, remaining - candidates[i], i, combination, result)
            combination.pop()

a = Solution()
print(a.combination_sum([2,3,6,7], 7))
