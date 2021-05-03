class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0:
            return []
        r,c = len(matrix), len(matrix[0])
        p = [[0]*c for i in range(r)]
        a = [[0]*c for i in range(r)]
        
        def dfs(x,y,h,vis):
            if x<0 or x>=r or y<0 or y>=c:
                return 
            if vis[x][y] or matrix[x][y] < h:
                return
            h = matrix[x][y]
            vis[x][y] = True
            dfs(x-1,y,h,vis)
            dfs(x,y-1,h,vis)
            dfs(x+1,y,h,vis)
            dfs(x,y+1,h,vis)
        
        for i in range(c):
            dfs(0,i,0,p)
            dfs(r-1,i,0,a)
        for i in range(r):
            dfs(i,0,0,p)
            dfs(i,c-1,0,a)
        
        res = []
        for i in range(r):
            for j in range(c):
                if p[i][j] and a[i][j]:
                    res.append((i,j))
        return res
                
        