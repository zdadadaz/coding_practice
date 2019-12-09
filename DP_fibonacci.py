
class fibo():
    # O(2^n)
    def fibo_naive(self, n):
        if n==0 or n== 1:
            return n
        return self.fibo_naive(n-1) + self.fibo_naive(n-2)
    
    def fibo_mem(self,n):
        arr = [0]*(n+1)
        arr[1] = 1
        return self.fibo_mem_recur(n,arr)
    
    def fibo_mem_recur(self,n,arr):
        if arr[n] != 0 or n == 0:
            return arr[n]
        else:
            arr[n] = self.fibo_mem_recur(n-1,arr)+self.fibo_mem_recur(n-2,arr)
        return arr[n]

    def fibo_bottom_up(self,n):
        arr = [0]*(n+1)
        arr[1] = 1
        if n == 0 or n == 1:
            return arr[n]
        i = 2
        while i <= n:
            arr[i] = arr[i-1]+arr[i-2]
            i += 1
        return arr[n]
sol = fibo()
A = 6
print(sol.fibo_bottom_up(A))
