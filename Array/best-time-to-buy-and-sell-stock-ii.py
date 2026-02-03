# lc 122
class Solution:
    # 题目要求只要保持1股就行, 可以同一天可以卖股票后再买股票,
    # 所以只要明天比今天涨，我就赚这个差价。累加所有上升段
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit