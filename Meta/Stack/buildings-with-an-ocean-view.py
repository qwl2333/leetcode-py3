# lc 1762
class Solution:
    # 单调栈解法 time O(n), space O(n)
    def findBuildings(self, heights: list[int]) -> list[int]:
        stack = []
        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop()
            stack.append(idx)
        return stack

s = Solution()
print(s.findBuildings([4,2,3,1]))