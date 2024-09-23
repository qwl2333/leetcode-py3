# lc 973
from heapq import heappush, heappop
class Solution:
    # time O(nlogk) space O(k)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_q = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heappush(max_q, (-distance, x, y))
            if len(max_q) > k:
                heappop(max_q)

        return [[x, y] for _neg_d, x, y in max_q]