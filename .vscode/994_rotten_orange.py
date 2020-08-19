class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        h = len(grid)
        w = len(grid[0])
        fresh = 0
        rotten = []
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    rotten.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
            
        t = 0
        while len(rotten)>0:
            rot_size = len(rotten)
            for i in range(rot_size):
                x,y = rotten[0] # pop the first rotten 
                rotten.pop(0)
                if x > 0 and grid[x-1][y]==1:
                    grid[x-1][y]=2
                    fresh -=1
                    rotten.append([x-1,y])
                if y > 0 and grid[x][y-1]==1:
                    grid[x][y-1]=2
                    fresh -=1
                    rotten.append([x,y-1])
                if x < h-1 and grid[x+1][y]==1:
                    grid[x+1][y]=2
                    fresh -=1
                    rotten.append([x+1,y])
                if y < w-1 and grid[x][y+1]==1:
                    grid[x][y+1]=2
                    fresh -=1
                    rotten.append([x,y+1])
            if len(rotten)>0:
                t+=1
        return t if fresh==0 else -1
                    
                
        
    def bfs(self, i,j,fresh):
        from collections import deque
        queue = deque()
        queue.append((i,j))
        minute = 0
        vis = []
        while len(queue)>0:
            cur = queue.popleft()
            minute += 1
            print(cur)
            self.grid[cur[0]][cur[1]] = 0
            for a in self.gen_action(cur[0],cur[1]):
                if a not in vis:
                    queue.append(a)
                    vis.append(a)
                    fresh[0]-=1
        return minute
    
    def gen_action(self, i,j):
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for d in directions:
            newi = i + d[0]
            newj = j + d[1] 
            if newi >= 0 and newi < self.h and newj >= 0 and newj < self.w:
                if self.grid[newi][newj] == 1:
                    yield (newi,newj)

            
            
        