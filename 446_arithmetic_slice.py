class Solution:
    # TLE O(N^2)
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n <3:
            return 0
        cnt = 0
        for i in range(3, n+1):
            for j in range(n-i+1):
                if self.isarithmetic(A[j:j+i]):
                    cnt +=1
        return cnt
    
    def isarithmetic(self, arr):
        diff = arr[0]-arr[1]
        m = len(arr)
        for i in range(1,m-1):
            if arr[i]- arr[i+1]!=diff:
                return False
        return True

    # O(N^2) -> prio dp,but not dp
    def numberOfArithmeticSlices_heirachy(self, A: List[int]) -> int:
        n = len(A)
        if n <3:
            return 0
        arr = [0]*n
        i =3
        cnt = 0
        for j in range(n-i+1):
            if self.isarithmetic(A[j:j+i]):
                arr[j] = 1
        cnt = sum(arr)
        for i in range(4, n+1):
            for j in range(n-i+2):
                arr[j] = arr[j]*arr[j+1]
            cnt += sum(arr)        
        return cnt

    # O(N^2)
    def numberOfArithmeticSlices_better_brute_force(self, A: List[int]) -> int:
        n = len(A)
        cnt = 0
        for s in range(n-2):
            diff = A[s+1]-A[s]
            for i in range(s+2,n):
                if A[i]-A[i-1] == diff:
                    cnt+=1
                else:
                    break
        return cnt
    
    # O(N) recursion
    def numberOfArithmeticSlices_recursion(self, A: List[int]) -> int:
        n = len(A)
        self.cnt = 0
        def dfs(i):
            if i < 2:
                return 0
            ap = 0
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                ap = 1 + dfs(i-1)
                self.cnt +=ap
            else:
                dfs(i-1)
            return ap
        dfs(n-1)
        return self.cnt

# O(N) DP
    def numberOfArithmeticSlices_dp(self, A: List[int]) -> int:
        n = len(A)
        dp = [0]*n
        res = 0
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i] = 1+ dp[i-1]
                res += dp[i]
        return res