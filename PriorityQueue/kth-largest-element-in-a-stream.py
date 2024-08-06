# lc 703
from heapq import heappop, heappush
class KthLargest:
    # O(nlogk)
    def __init__(self, k: int, nums: list[int]):
        self.min_q = []
        self.k = k
        for num in nums:
            heappush(self.min_q, num)
            if len(self.min_q) > k:
                heappop(self.min_q)
    # O(logk)
    def add(self, val: int) -> int:
        heappush(self.min_q, val)
        if len(self.min_q) > self.k:
            heappop(self.min_q)
        return self.min_q[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)