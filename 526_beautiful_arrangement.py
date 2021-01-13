class Solution:
    def countArrangement(self, n: int) -> int:
        vis = [0]*16
        def dfs(s):
            if len(s) == n:
                return 1
            idx = len(s)+1
            res = 0
            for i in range(1,n+1):
                if vis[i] == 0:
                    if i%idx ==0 or idx%i==0:
                        vis[i] = 1
                        res += dfs(s+[i])
                        vis[i] = 0
            return res
        return dfs([])