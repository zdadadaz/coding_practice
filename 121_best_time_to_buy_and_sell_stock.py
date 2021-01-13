class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        gMax =0
        cMax = 0
        cur = 0
        for i in range(1,len(prices)):
            cMax = prices[i]-prices[cur]
            if cMax > gMax:
                gMax = cMax
            if cMax < 0:
                cur = i
        return gMax