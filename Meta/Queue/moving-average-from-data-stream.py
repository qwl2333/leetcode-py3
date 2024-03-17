# lc 346
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size_limit = size
        self.queue = deque()
        self.sum = 0

    # Time O(1), space O(k)
    def next(self, val: int) -> float:
        self.sum += val
        self.queue.append(val)
        if len(self.queue) > self.size_limit:
            removed_value = self.queue.popleft()
            self.sum -= removed_value
        
        return self.sum / len(self.queue)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)