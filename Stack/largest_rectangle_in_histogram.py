# lc 84 https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode
class Solution:
    # Neetcode 解法， 单调栈，单调栈最终里面的值都是单调增或减的，但是实际上所有的元素其实都进入过栈，这就有计算面积的可能性 time O(n), space O(n)
    # 思路就是：入栈的时候思考 当前的height 大于或等于 top of the stack吗，大于等于就可以入栈，小于top of the stack
    # 就出栈，出栈的时候计算面积，stack里面记录两个一个index，一个height，但是这个index要记住是可以向左extend直到stack里面所有
    # 大于当前height的都pop出来了，此时的最近pop的index 才是start index，意味着当前height可以一直向左extend到此时的index
    # 此题复杂，记住就好
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area