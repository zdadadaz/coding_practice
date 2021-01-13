class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans        
    
    # TLE
    def recur(self,n,k,vis,kcount,ans):
        if len(vis)==n:
            kcount[0] += 1
            if kcount[0] == k:
                ans.append(''.join(vis))
            return
        else:
            for i in range(1,n+1):
                if str(i) not in vis:
                    self.recur(n,k,vis+[str(i)],kcount,ans)
                    if kcount[0] == k:
                        return ans[0]