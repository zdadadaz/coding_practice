class Solution:
    # memory
    def climbStairs_recursion(self, n: int) -> int:
        mem = [0]*n
        def dfs(cur, mem):
            if cur == n:
                return 1
            if cur > n:
                return 0
            if mem[cur] > 0:
                return mem[cur]
            
            mem[cur] = dfs(cur+1,mem) + dfs(cur+2,mem)
            return mem[cur]
        
        return dfs(0, mem)

    def climbStairs_dp(self, n: int) -> int:
        if n<=3:
            return n
        mem = [0]*(n+1)
        mem[1] = 1
        mem[0] = 0
        mem[2] = 2
        for i in range(3, n+1):
            mem[i] = mem[i-1] + mem[i-2]
        return mem[-1]