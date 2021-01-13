class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[999999]*(len(dungeon[0])+1) for i in range(len(dungeon)+1)]
        dp[-1][-2],dp[-2][-1] = 1,1
        
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[i])-2,-1,-1):
                # not allow minus blood, reset the blood
                dp[i][j] = max(1,min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]
        