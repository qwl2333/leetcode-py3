# lc 121

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        smlst_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            if prices[i] > smlst_price:
                max_profit = max(max_profit, prices[i] - smlst_price)
            else:
                smlst_price = prices[i]
        return max_profit

a = Solution()
print(a.maxProfit([7, 1 , 5 , 3 , 6, 4]))