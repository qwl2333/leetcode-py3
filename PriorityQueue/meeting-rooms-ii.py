# lc 253
from heapq import heappop, heappush
class Solution:
    # Time O(nlogn) n - len of intervals, space O(n) worst case all intervals in min_heap
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        min_heap = [] # keep track of the end time of the rooms, head is the room with earliest end time
                      # how many end times in min_heap stands for how many rooms are currently used
                      # so we can also use room_counter = len(min_heap) to get number of rooms
        room_counter = 0
        intervals.sort(key=lambda i: i[0])
        for s, e in intervals:
            if not min_heap:
                heappush(min_heap, e)
                room_counter += 1
                continue
            if s < min_heap[0]:
                heappush(min_heap, e)
                room_counter += 1
            else:
                heappop(min_heap)
                heappush(min_heap, e)
        return room_counter

s = Solution()
print(s.minMeetingRooms([[0,30],[5,10],[5,10],[5,10],[15,20]])) # 4 rooms