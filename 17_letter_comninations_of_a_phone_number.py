class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.vis =[]
        n = len(digits)
        if n == 0:
            return []
        m = {'2':'abc','3':'def','4':'ghi', '5':'jkl','6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        def dfs(d, s):
            if d ==n:
                self.vis.append(''.join(s))
                return 
            for i in m[digits[d]]:
                dfs(d+1, s+[i])
        dfs(0,[])
        return self.vis