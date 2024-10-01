# lc 875
from math import ceil
class Solution:
    # O(nlogm) n - number of pile in piles, m - max pile in piles
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        total_bananas = sum(piles)
        l_speed = total_bananas // h
        u_speed = max(piles)

        def can_finish(speed: int, h: int) -> bool:
            if speed == 0:
                return False
            count = 0
            for pile in piles:
                count += int(ceil(pile / speed))

            return True if count <= h else False
    
        while l_speed <= u_speed:
            mid_speed = (l_speed + u_speed) // 2
            if can_finish(mid_speed, h):
                u_speed = mid_speed - 1
            else:
                l_speed = mid_speed + 1

        return l_speed

s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))