# lc 362
from collections import deque
class HitCounter:

    def __init__(self):
        self.windown_length = 300
        self.time_hits = deque()
        self.num_of_hits = 0

    def hit(self, timestamp: int) -> None:
        if not self.time_hits: # time_hits empty
            self.time_hits.append([timestamp, 1])
            self.num_of_hits += 1
            return
        
        if self.time_hits[-1][0] == timestamp:
            self.time_hits[-1][1] += 1
        else:
            self.time_hits.append([timestamp, 1])
        self.num_of_hits += 1
        
        while self.time_hits[0][0] <= timestamp - self.windown_length:
            _ts, hits = self.time_hits.popleft()
            self.num_of_hits -= hits

    def getHits(self, timestamp: int) -> int:
        while self.time_hits and self.time_hits[0][0] <= timestamp - self.windown_length:
            _ts, hits = self.time_hits.popleft()
            self.num_of_hits -= hits
        
        return self.num_of_hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)