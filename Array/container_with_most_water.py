# lc 11

class Solution:
    # Brute force - TLE
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        max_area = 0
        for l in range(0, n):
            for r in range(l + 1, n):
                area = min(height[l], height[r]) * (r - l)
                max_area = max(area, max_area)
        
        return max_area

    # Greedy
    def maxArea2(self, height: list[int]) -> int:
        n = len(height)
        max_area = 0
        l, r = 0, n - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                # 左右相等时，走那边都无所谓，因为假如有更大的area，一定不会有这俩边里任何一个
                l += 1
        
        return max_area