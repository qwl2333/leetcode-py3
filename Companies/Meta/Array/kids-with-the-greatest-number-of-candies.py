# lc 1431:
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # 1. 找到当前的最大值（这就是我们的标杆）
        # 时间复杂度 O(N)
        max_val = 0
        for c in candies:
            max_val = max(max_val, c)

        res = []
        # 对每一个 c，检查 c + extraCandies 是否 >= max_val
        for c in candies:
            if c + extraCandies >= max_val:
                res.append(True)
            else:
                res.append(False)
        
        return res
