class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        buy = prev_buy = -prices[0]
        sell = prev_sell = 0
        hold = prev_hold = 0
        for i in range(len(prices)):
            hold = max(prev_hold, prev_sell)
            buy = max(prev_buy, prev_hold - prices[i])
            sell = max(prev_sell, prev_buy + prices[i])
            prev_hold, prev_buy, prev_sell = hold, buy, sell
        return sell
            