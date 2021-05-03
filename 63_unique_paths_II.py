class Solution:
    
    def uniquePathsWithObstacles_TLE(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        que = [(0,0)]
        res = 0
        move = [1,0,1]
        while que:
            cur = que.pop()
            if cur==(r-1,c-1):
                res +=1
            for i in range(2):
                x = cur[0]+move[i]
                y = cur[1]+move[i+1]
                if 0<=x<r and 0<=y<c and obstacleGrid[x][y]!=1:
                    que.append((x,y))
        return res


    def uniquePathsWithObstacles_DP(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        dp = [[0]*c for i in range(r)]
        dp[0][0] = 1
        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 0
        return dp[r-1][c-1]

    def uniquePathsWithObstacles_constant_space(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0] = 1
        # initial col
        for i in range(1, r):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0]==1)
        # initial row
        for i in range(1, c):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1]==1)
        
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[r-1][c-1]
                    