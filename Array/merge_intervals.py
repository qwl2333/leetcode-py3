# lc 56

class Solution:
    # T: O(n), S: worst case O(n) n -> len of intervals
    # 此题核心就是发现两个分开的interval, 把前面那个interval的放进res里面
    # 如果是有overlap,就要把两个interval融合成一个通过prev_e = max(prev_e, cur_e)
    # 然后再继续找两个分开的interval
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])
        prev_s, prev_e = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i][0], intervals[i][1]
            if cur_s <= prev_e:
                prev_e = max(prev_e, cur_e)
            else: # cur_s > prev_e
                res.append([prev_s, prev_e])
                prev_s = cur_s
                prev_e = cur_e
        
        res.append([prev_s, prev_e])
        return res

a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))