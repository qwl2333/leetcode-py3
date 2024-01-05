# lc 121

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        i = 0 # index to track the min value in prices, could be replaced with value instead of index
        j = 1 # index to iterate the prices array
        while j < n:
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                j += 1
            else:
                i = j
                j = i + 1
        
        return max_profit

a = Solution()
print(a.max_profit([7, 1 , 5 , 3 , 6, 4]))