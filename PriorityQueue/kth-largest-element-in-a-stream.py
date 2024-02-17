# lc 703
from queue import PriorityQueue
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.pq = PriorityQueue()
        self.k = k
        for num in nums:
            self.pq.put(num)

        while self.pq.qsize() > k:
            self.pq.get()


    def add(self, val: int) -> int:
        self.pq.put(val)
        if self.pq.qsize() > self.k:
            self.pq.get()
        return self.pq.queue[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)