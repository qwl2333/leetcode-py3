# lc 56

class Solution:
    # T: O(n), S: worst case O(n) n -> len of intervals
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])

        res = []

        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= cur_end:
                cur_end = max(intervals[i][1], cur_end)
            else: # intervals[i][0] > cur_end
                res.append([cur_start, cur_end])
                cur_start = intervals[i][0]
                cur_end = intervals[i][1]
            i += 1

        res.append([cur_start, cur_end])
        return res

a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))