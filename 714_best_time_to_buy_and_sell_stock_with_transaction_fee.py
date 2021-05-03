class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, sold = float('-inf'), 0
        for p in prices:
            hold2,sold2 = hold, sold
            hold = max(hold2, sold2-p)
            sold = max(sold2, hold2+p-fee)
        return sold