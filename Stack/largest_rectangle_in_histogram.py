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
            while stack and stack[-1][1] > h: #这里>=或者>都可以pass，但是方便理解 h必须严格小于top of stack，这意味着top of stack的height的矩形右边边界找到了
                index, height = stack.pop() # 每次pop完都要计算pop出来的height可以得到的最大居心
                max_area = max(max_area, height * (i - index)) # i是左边界，i所在的h是严格小于pop出的height的，你可能好奇为啥是i-index，假如stack是（0，5），（1，5‘），当前i是2，h是3，这次pop（1，5’），可以得出当前5‘为高，左边从1开始到i=2位置但不含2的矩形面积5，下次还会pop （0， 5），就是以5为高，从0开始到i=2但不含2的矩形面积10，所以相等的情况也不会漏掉
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area

a = Solution()
print(a.largestRectangleArea([2, 5, 6, 2, 3]))