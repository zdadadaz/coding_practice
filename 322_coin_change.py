class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = amount+1
        dp = [float('inf')]*n
        dp[0]=0
        for i in range(1,n):
            for c in coins:
                if i-c>=0:
                    if dp[i] == float('inf'):
                        dp[i] = dp[i-c]+1
                    else:
                        dp[i] = min(dp[i], 1 + dp[i-c])
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]