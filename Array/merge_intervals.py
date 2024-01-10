# lc 56

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []

        intervals.sort(key=lambda item: item[0])

        start = intervals[0][0] # start end are used to create the merged interval for the result
        end = intervals[0][1]
        for i in range(len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if cur_start <= end:
                end = max(end, cur_end)
            else:
                result.append([start, end])
                start = cur_start
                end = cur_end
        
        result.append([start, end])

        return result

a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))