# lc 1046
from queue import PriorityQueue
class Solution:
    # Time O(nlogn) n - len of stones, Space O(n)
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_q = PriorityQueue()
        for stone in stones:
            max_q.put((-stone, stone))
        
        while max_q.qsize() > 1:
            _priority1, stone_val1 = max_q.get()
            _priority2, stone_val2 = max_q.get()
            stone_val1 -= stone_val2
            if stone_val1 > 0:
                max_q.put((-stone_val1, stone_val1))
        
        if max_q.empty():
            return 0
        else:
            return max_q.queue[0][1]