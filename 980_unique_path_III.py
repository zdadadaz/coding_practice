class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        tot = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    start = (i,j)
                if grid[i][j]==2:
                    finish =(i,j)
                if grid[i][j]>=0:
                    tot+= 1
        grid[start[0]][start[1]] = -2
        out = []
        self.dfs(start, finish, [start], out, grid, tot)
        return len(out)
        
    def dfs(self, cur, finish, vis, out, grid, tot):
        if cur[0]==finish[0] and cur[1]==finish[1] and len(vis)== tot:
            out.append(vis)
            return
        else:
            for a in [(-1,0),(0,-1),(1,0),(0,1)]:
                newx = cur[0]+a[0]
                newy = cur[1]+a[1]
                if newx>=0 and newx< len(grid) and newy>=0 and newy < len(grid[0]) and grid[newx][newy] >= 0:
                    tmp = grid[newx][newy]
                    grid[newx][newy] = -2
                    new = (newx, newy)
                    self.dfs(new,finish, vis+[new], out, grid, tot)
                    grid[newx][newy] = tmp
    