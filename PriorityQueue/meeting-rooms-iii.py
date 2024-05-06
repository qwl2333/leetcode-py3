from heapq import heappop, heappush, heapify
# lc 2402
class Solution:
    # T: O(nlogn + mlogn) n - number of rooms, m - number of meetings
    # S: O(n) for heaps, two heaps will at most have n meetings inside
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        heapify(available)
        used = [] # (end_time, room_number)
        count = [0 for _ in range(n)]

        for start, end in meetings:
            while used and used[0][0] <= start: # is there any used room becoming available before or at current start time
                _, room = heappop(used)
                heappush(available, room)
            
            if not available:
                end_time, room = heappop(used)
                end = end_time + (end - start) # new end time
                heappush(available, room)
            
            room = heappop(available)
            heappush(used, (end, room))
            count[room] += 1
        
        return count.index(max(count)) # return the lowest room with max meetings scheduled

s = Solution()
print(s.mostBooked(2, [[0,10],[0,10],[0,15],[2,7],[3,4]]))
