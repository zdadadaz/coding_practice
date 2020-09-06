class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp= [365*costs[0]]*(n+1) # maximum value
        dp[-1]=0
        for i in range(n-1,-1,-1):
            d7,d30=i,i
            while d7 < n and days[d7]< (days[i]+7): d7+=1
            while d30 < n and days[d30]< (days[i]+30): d30+=1
            dp[i] = min(costs[0]+dp[i+1], costs[1]+dp[d7],costs[2]+dp[d30])
        return dp[0]