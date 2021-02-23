class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        r,c = len(grid), len(grid[0])
        que = [(0,0)]
        vis = set([(0,0)])
        cnt = 0
        dirs= [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0),(1,1)]
        while que:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur ==(r-1,c-1):
                    return cnt+1
                for i,j in dirs:
                    x = cur[0]+i
                    y = cur[1]+j
                    if 0<=x<r and 0<=y<c and grid[x][y]==0 and (x,y) not in vis:
                        que.append((x,y))
                        vis.add((x,y)) # -> should be inside the loop, otherwise TLE
            cnt +=1
        return -1