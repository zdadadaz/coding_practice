class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0]*m for i in range(n)]
        for i in range(m):
            mat[n-1][i] = 1
        for j in range(n):
            mat[j][m-1] = 1
            
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                mat[j][i] = mat[j+1][i] + mat[j][i+1]
        print(mat)
        return mat[0][0]
        
    #     self.move = [(0,(1,0)),(1,(0,1))]
    #     vis = []
    #     self.dfs(m,n,vis,(1,1),[],{})
    #     return len(vis)
    # def dfs(self,m,n,vis,cur,path,_V):
    #     if cur ==(m,n) and path not in vis:
    #         vis.append(path)
    #         return 1
    #     else:
    #         if cur not in _V:
    #             acc = 0
    #             for a in [i for i in self.move if cur[0]+i[1][0]<=m and cur[1]+i[1][1]<=n]:
    #                 acc+=self.dfs(m,n,vis,(cur[0]+a[1][0], cur[1]+a[1][1]),path+[a[0]],_V)
    #             _V[cur] = acc
    #         return _V[cur]