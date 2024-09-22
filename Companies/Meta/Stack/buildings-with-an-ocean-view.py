# lc 1762
class Solution:
    # 单调栈解法 time O(n), space O(n)
    def findBuildings(self, heights: list[int]) -> list[int]:
        stack = []
        i = 0
        while i < len(heights):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
            i += 1
        return stack

s = Solution()
print(s.findBuildings([4,2,3,1]))