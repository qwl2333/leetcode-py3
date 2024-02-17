# lintcode 391 给了很多飞机的起落时间，问天空中最多同时有多少飞机
# https://blog.csdn.net/u013325815/article/details/103388203
# 解题思路是sweep line算法，把飞机的起和落分别看成一个event
# [1,10] 1点飞，10点落可以看成两个event (1, 1), (10, -1)
# 全部按照时间排序，但是如果在同一个时间既有起飞，也有降落，那先算降落的，所以降落排在前
from queue import PriorityQueue
class Solution:
    """
    @param airplanes: an array of taking off and landing time of airplanes
    @return: the max number of airplanes in the sky at the same time
    """
    def countOfAirplanes(self, airplanes):
        # Write your code here
        sky = PriorityQueue()
        # 加入开始时间和结束时间，1是飞机起飞+1，-1是飞机降落-1
        # priority queue 先按照start，landing排序，再按照-1，1 排序，相同时间，-1排在前
        for start, landing in airplanes:
            sky.put((start, 1))
            sky.put((landing, -1))

        #扫描一遍
        ans = 0
        count = 0
        while not sky.empty():
            time, direction = sky.get()
            print(f'time: {time}, direction: {direction}')
            count += direction
            ans = max(ans, count)
        return ans

s = Solution()
print(s.countOfAirplanes([(1, 10), (2, 3), (5, 8), (3, 7)]))