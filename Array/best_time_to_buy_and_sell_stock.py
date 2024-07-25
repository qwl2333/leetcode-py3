# lc 121

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        i, j = 0, 1
        max_profit = 0
        while j < n:
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
            
            if prices[j] < prices[i]:
                i = j
            
            j += 1
        
        return max_profit

# max_profit 0
# i: left smallest price idx
# j: right biggest price idx
# [7,1,5,3,6,4]
# i 0
# j 1
# update max_profit if prices[j] - prices[i] > max_profit
# update i if prices[j] < prices[i]

a = Solution()
print(a.maxProfit([7, 1 , 5 , 3 , 6, 4]))