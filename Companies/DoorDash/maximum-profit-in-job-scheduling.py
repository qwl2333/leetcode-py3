class Solution:
    # time O(nlogn) since we use binary search n - length of arrays
    # space O(n) caching and new intervals we created
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        # [(1,3,50), (2,4,10), (3,5,40), (3,6,70)]
        cache = {} # max margin we can get if starting from i of intervals

        def dfs(i): # start from i, i is the index of intervals, find the largest profit
            if i == len(intervals) or i == -1:
                return 0
            if i in cache:
                return cache[i]

            # if not selecting intervals[i], move to the next
            res = dfs(i + 1)

            # if selecting intervals[i], find next legit interval and get the profit[j] + profit[i]
            j = binary_search(i + 1, len(intervals) - 1, intervals[i][1])


            # Now j is either a legit interval or out of bound len(intervals)
            # include or not, find the max
            res = max(res, dfs(j) + intervals[i][2])
            cache[i] = res
            return res
        
        # find first in intervals that start >= target
        def binary_search(start: int, end: int, target: int) -> int:
            if start > end:
                return -1

            while start <= end:
                mid = (start + end) // 2
                if intervals[mid][0] >= target:
                    end = mid - 1
                else: # intervals[mid][0] < target
                    start = mid + 1

            if start < len(intervals):
                return start
            else:
                return -1
            
        return dfs(0)

s = Solution()

print(s.jobScheduling(startTime=[1,2,3,3], endTime=[3,4,5,6], profit=[50,10,40,70]))
