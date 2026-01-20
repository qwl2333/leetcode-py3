# lc 84 https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode
# lc 42 类似
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # 1. 技巧：前后加哨兵 (高度为 0)
        # 前面的 0 保证栈永远不会为空（作为最左侧的边界）
        # 后面的 0 保证遍历结束时能强制弹出栈内所有剩余柱子并结算
        heights = [0] + heights + [0]
        stack = [] # 存储柱子的下标 (索引)
        max_area = 0
        
        for i, h in enumerate(heights):
            # 当遇到当前柱子高度 < 栈顶柱子高度时，说明找到了栈顶柱子的“右边界”
            while stack and h < heights[stack[-1]]: # 在前面加入的哨兵0是永远不可能被弹出的，因为没有哪个柱子高度会 < 0，这就保证了stack永远不空
                # 1. 弹出栈顶作为当前矩形的高度
                h_idx = stack.pop()
                cur_h = heights[h_idx]
                
                # 2. 此时的新栈顶就是该柱子的“左边界”
                # 因为栈是单调递增的，左边第一个比它矮的一定是新栈顶
                left_idx = stack[-1]
                right_idx = i
                
                # 3. 计算宽度和面积
                width = right_idx - left_idx - 1
                max_area = max(max_area, cur_h * width)
            
            # 保持栈内下标对应的高度是单调递增的
            stack.append(i)
            
        return max_area

a = Solution()
print(a.largestRectangleArea([2, 5, 6, 2, 3]))