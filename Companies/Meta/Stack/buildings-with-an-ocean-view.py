# lc 1762
class Solution:
    # 单调栈解法 time O(n), space O(n)
    def findBuildings(self, heights: list[int]) -> list[int]:
        stack = []
        i = 0
        while i < len(heights):
            # 最难的就是这个>=等号, [4,2,2‘,1] 返回 [0,2,3]
            # 意思是2是看不到海边的因为被2'挡住了
            # 所以如果当前高度== stack最后一个元素的高度，需要把那个元素pop出来
            # 加上等号是一个严格递减的单调栈
            # 不加上等号是一个不严格递减的单调栈
            while stack and heights[i] >= heights[stack[-1]]:                 
                stack.pop()
            stack.append(i)
            i += 1
        return stack

s = Solution()
print(s.findBuildings([4,2,3,1]))