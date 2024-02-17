# https://leetcode.com/discuss/interview-question/4220278/Amazon-OA
from queue import PriorityQueue
class Solution:
    # time O(nlogn)
    def min_fruits_left(self, fruits: list[int]) -> int:
        freq_map = {}
        for fruit in fruits:
            freq_map[fruit] = freq_map.get(fruit, 0) + 1

        pq = PriorityQueue()
        for fruit_type, frequency in freq_map.items():
            pq.put((-frequency, (frequency, fruit_type)))
        
        while pq.qsize() > 1:
            _minus_freq_1, (freq_1, fruit_type_1) = pq.get()
            _minus_freq_2, (freq_2, fruit_type_2) = pq.get()
            freq_1 -= 1
            freq_2 -= 1
            if freq_1 > 0:
                pq.put((-freq_1, (freq_1, fruit_type_1)))
            if freq_2 > 0:
                pq.put((-freq_2, (freq_2, fruit_type_2)))
        if pq.qsize() == 1:
            return -pq.get()[0]
        else:
            return 0

s = Solution()
print(s.min_fruits_left([9,7,8,9,9,9,9]))
