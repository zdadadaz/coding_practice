class Solution:
    # TLE
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [Counter(s) for s in strs]
        self.max = 0
        def dfs(vis, m,n):
            if m>=0 and n>=0:
                self.max = max(self.max, len(vis))
            for idx,c in enumerate(counts):
                if c['0']>m or c['1']>n or idx in vis:
                    continue
                dfs(vis+[idx], m-c['0'], n -c['1'])
        dfs([],m,n)
        return self.max

    def findMaxForm_dp(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(m+1) for i in range(n+1)]
        for s in strs:
            c = Counter(s)
            for i in range(n, c['1']-1,-1):
                for j in range(m, c['0']-1,-1):
                    dp[i][j] = max(dp[i][j], dp[i-c['1']][j-c['0']]+1)
        return dp[n][m]