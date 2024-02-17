# 题目是 n种items, 每种无限多个，a=[2,1,1], b=[1,2,3], a,b是买一个item的花费
# cost = a[i] + (j - 1) * b[i], j是第j个type i item
# 买 m 次，多少花费
from queue import PriorityQueue
class Solution:
    # 用 pq
    def min_cost_to_purchase_m_items(self, a: list[int], b: list[int], m: int) -> int:
        pq = PriorityQueue()
        n = len(a)
        for i in range(n):
            pq.put((a[i], (1, a[i], b[i])))
        
        res = 0
        for i in range(m):
            cost, (seq, a_v, b_v) = pq.get()
            res += cost
            new_cost = a_v + seq * b_v
            pq.put((new_cost, (seq + 1, a_v, b_v)))
        
        return res

s = Solution()

print(s.min_cost_to_purchase_m_items([2,1,1], [1,2,3], 4))