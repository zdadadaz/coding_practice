class Solution:
    def numSquares(self, n: int) -> int:
        import math
        self.nn = int(math.sqrt(n))
        dp=[0]*(n+1)
        for x in range(1,n+1):
            min_val = x
            y,sq=1,1
            while sq <= x:
                min_val = min(min_val, 1+dp[x-sq])
                y+=1
                sq = y*y
            dp[x] = min_val
        return dp[n]
                
    # TTL
    def numSquares_recu(self,n):
        self.min = 9999999
        self._V = {}
        return self.recur(n,0,[],[])

    def recur(self,n,s,t,vis): # s:sum, t:path
        if len(t)> self.min:
            return 9999999
        if s == n and t not in vis:
            if len(t) < self.min:
                self.min = len(t)
            vis.append(t)
            return len(t)
        else:
            if tuple(t) not in self._V:
                self._V[tuple(t)] = min(self.recur(n,s+a*a,t+[a*a],vis) for a in range(self.nn,0,-1) if a*a+s<=n)
            return self._V[tuple(t)]