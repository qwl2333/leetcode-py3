# lc 295
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.low = [] # max neg
        self.high = [] # min

    def addNum(self, num: int) -> None:
        if not self.low:
            heappush(self.low, -num)
            return

        if num > -self.low[0]:
            heappush(self.high, num)
        else:
            heappush(self.low, -num)

        if len(self.low) - len(self.high) > 1:
            heappush(self.high, -self.low[0])
            heappop(self.low)
        elif len(self.high) - len(self.low) > 0:
            heappush(self.low, -self.high[0])
            heappop(self.high)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

sol = MedianFinder()
sol.addNum(2)
sol.addNum(2)
sol.addNum(3)
sol.addNum(3)
print(sol.findMedian())