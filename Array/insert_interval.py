# lc 57

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        new_interval_inserted = False
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                if not new_interval_inserted:
                    result.append(newInterval)
                    new_interval_inserted = True
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
    
        if not new_interval_inserted:
            result.append(newInterval)
        

        return result  
    
a = Solution()
print(a.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))





            
            
        



