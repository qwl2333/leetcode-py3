# lc 252
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])
        for i in range(len(intervals) - 1):
            start_i, end_i = intervals[i]
            start_i_next, end_i_next = intervals[i + 1]
            if end_i > start_i_next:
                return False

        return True

s = Solution()
print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))