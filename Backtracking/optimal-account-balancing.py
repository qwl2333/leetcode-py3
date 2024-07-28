# lc 465 time O(n!) because T(n) = n * T(n - 1), every recursion we run n iterations, each iteration it because T(n - 1), etc.
from queue import PriorityQueue
class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        ids_to_debt = [0 for _ in range(12)]

        for from_i, to_i, amount in transactions:
            ids_to_debt[from_i] -= amount
            ids_to_debt[to_i] += amount

        debts = []
        for debt in ids_to_debt:
            if debt != 0:
                debts.append(debt)

        self.res = float('inf')
        n = len(debts)
        def dfs_to_settle(idx, steps): # [0, idx - 1] has been settled, now settle current debts[idx] with any value from debts[idx + 1] to debts[n - 1]
            if idx == n:
                self.res = min(self.res, steps)
                return
            
            if debts[idx] == 0:
                return dfs_to_settle(idx + 1, steps)

            for i in range(idx + 1, n):
                if debts[idx] * debts[i] < 0: # only settle debts[idx] with opposite value
                    debts[i] += debts[idx]
                    dfs_to_settle(idx + 1, steps + 1)
                    debts[i] -= debts[idx]

        dfs_to_settle(0, 0)
        return self.res