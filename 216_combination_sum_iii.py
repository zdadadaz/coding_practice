
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.dfs(k,n,0,0,[],[i for i in range(1,10)])
        return self.res
    
    def dfs(self,k,n,s,t,tlist,numlist):
        if s>k:
            return
        if s==k and t==n:
            self.res.append(tlist)
            return
        for idx, i in enumerate(numlist):
            self.dfs(k,n,s+1,t+i,tlist+[i],numlist[idx+1:])