class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k<=0 or not prices:
            return 0
        N = len(prices)
        if k>=N:
            profit = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        
        buy = [float('-inf')]*(k+1)
        sell = [0]*(k+1)
        for i in range(N):
            for j in range(1,k+1):
                buy[j] = max(buy[j], sell[j-1]-prices[i])
                sell[j] = max(sell[j], buy[j]+prices[i])
        return sell[-1]
