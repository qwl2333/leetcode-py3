# lc 973
from queue import PriorityQueue
class Solution:
    # time O(nlogn) space O(n) n - len(points)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_q = PriorityQueue()
        for x, y in points:
            min_q.put((x ** 2 + y ** 2, [x, y]))
        
        res = []
        for i in range(k):
            res.append(min_q.get()[1])
        
        return res