# T(n) = T(n-1)+T(n-2)+..+T(1)
# T(n+1) = T(n) + T(n-1) + ... + T(1)
# T(n+1) = 2T(n)
# T(n) = 2^n
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res
    
    def dfs(self, s, temp):
        if not s:
            self.res.append(temp[:])
            return 
        for i in range(1, len(s)+1):
            if self.isPan(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:], temp)
                temp.pop()
    
    def isPan(self, s):
        return s == s[::-1]