'''Say you have an array for which the ith element is the price of a given stock on day i.  Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).  After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        prices_len = len(prices)
        
        if prices_len < 2:
            return 0
    
        prev_buy, prev_sell, prev_nothing = -prices[0], 0, 0
        
        for i in range(1, prices_len):
            buy  = max(prev_nothing - prices[i], prev_buy) 
            sell = max(prev_buy + prices[i], prev_sell)
            nothing = max(prev_sell, prev_buy, prev_nothing)
            prev_buy, prev_sell, prev_nothing = buy, sell, nothing
        return max(sell, nothing)
        
inputZ = [1,2,3,0,2]
outputZ = 3
print(maxProfit(inputZ), "should equal", outputZ)
