# lc 1779
# 此题无聊，可以不看
class Solution:
    # time O(n)
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        smlst_dist = float('inf')
        index = -1
        for i, point in enumerate(points):
            if point[0] != x and point[1] != y:
                continue

            m_dist = abs(point[0] - x) + abs(point[1] - y)
            if m_dist < smlst_dist:
                smlst_dist = m_dist
                index = i
            elif m_dist == smlst_dist:
                index = min(index, i)
        
        return index
