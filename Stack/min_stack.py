# lc 155

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # 单调的不严格递减的栈

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]: # 为什么相等要放进去,因为可能最小值有多个
            self.min_stack.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(1)
obj.push(-3)
obj.push(1)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
obj.pop()
param_5 = obj.top()
param_6 = obj.getMin()