# lc 232

class MyQueue:
    # 2 iterations when pop
    top_of_queue = None
    stack1 = None
    stack2 = None

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.top_of_queue = x
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 0: # 必须要一次性全从in 到 out, 如果只放一个, 后面如果有新的push进来, 顺序就乱了
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        self.top_of_queue = self.stack2[-1] if len(self.stack2) > 0 else None
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self) -> int:
        return self.top_of_queue

    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False
    
    # # 1 iteration
    # def __init__(self):
    #     self.stack_in = []
    #     self.stack_out = []

    # def push(self, x: int) -> None:
    #     self.stack_in.append(x)

    # def pop(self) -> int:
    #     self.peek()
    #     return self.stack_out.pop()

    # def peek(self) -> int:
    #     if len(self.stack_out) == 0:
    #         while len(self.stack_in) > 0:
    #             self.stack_out.append(self.stack_in.pop())
    #     return self.stack_out[-1]
        

    # def empty(self) -> bool:
    #     return len(self.stack_in) == 0 and len(self.stack_out) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()