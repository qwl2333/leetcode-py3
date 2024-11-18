# lc 986
class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i, j = 0, 0
        n = len(firstList)
        m = len(secondList)
        res = []
        while i < n and j < m:
            fst = firstList[i]
            scd = secondList[j]
            if self.has_intersection(fst, scd):
                new_s = max(fst[0], scd[0])
                new_e = min(fst[1], scd[1])
                res.append([new_s, new_e])
                if fst[1] > scd[1]:
                    j += 1
                elif fst[1] < scd[1]:
                    i += 1
                else: # fst[1] = scd[1]
                    i += 1
                    j += 1
            else: # no intersection
                if fst[1] > scd[1]:
                    j += 1
                else: # fst[1] < scd[1]
                    i += 1
                
        return res
    
    def has_intersection(self, first: list[int], second: list[int]) -> bool:
        if first[0] > second[1] or second[0] > first[1]:
            return False
        else:
            return True
    
s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))