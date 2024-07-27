# lc 252
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        n = len(intervals)
        if n == 0:
            return True
        intervals.sort(key=lambda i: i[0])
        prev_end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < prev_end:
                return False
            else:
                prev_end = intervals[i][1]

        return True

s = Solution()
print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))