# lc 1046
from heapq import heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_q = []
        for stone in stones:
            heappush(max_q, -stone)
        
        while len(max_q) > 1:
            stone1 = -heappop(max_q)
            stone2 = -heappop(max_q)
            remaining = abs(stone1 - stone2)
            if remaining!= 0:
                heappush(max_q, -remaining)
        
        if len(max_q) == 0:
            return 0
        else:
            return -max_q[0]