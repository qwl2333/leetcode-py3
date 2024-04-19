class Solution:
    # 双指针 一个指针在 jobs, 一个在worker，在jobs的指针是在记录最大的profit
    # Time O(nlogn + mlogm), n - len(difficulty), m - len(worker), space O(n) - new jobs array
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit)) # sorted by difficulty then profit
        worker = sorted(worker)
        profit_sum = 0
        i = 0
        max_profit = 0
        for w in worker:
            while i < len(jobs) and w >= jobs[i][0]:
               max_profit = max(max_profit, jobs[i][1]) 
               i += 1
            print(f'w: {w}')
            print(f'max_profit: {max_profit}')
            profit_sum += max_profit

        return profit_sum 

s = Solution()
print(s.maxProfitAssignment([2,2,3,3],[1,3,1,1],[1,2,2,3,3,4]))