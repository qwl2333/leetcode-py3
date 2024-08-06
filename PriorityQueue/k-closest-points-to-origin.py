# lc 973
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_q = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heappush(min_q, (distance, [x, y]))
        
        counter = 0
        res = []
        while counter < k:
            _d, coord = heappop(min_q)
            res.append(coord)
            counter += 1
        
        return res