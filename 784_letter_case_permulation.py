class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        letters = set([chr(i+ord('a')) for i in range(26)])
        self.res = []
        def dfs(vis, arr):
            if len(vis) ==n:
                self.res.append(''.join(vis))
                return
            for i,v in enumerate(arr):
                if v.lower() in letters:
                    dfs(vis+[v.upper()], arr[i+1:])
                dfs(vis+[v.lower()], arr[i+1:])
        dfs([],S)
        return self.res

    def letterCasePermutation_no_loop(self, S: str) -> List[str]:
        n = len(S)
        letters = set([chr(i+ord('a')) for i in range(26)])
        self.res = []
        def dfs(vis, idx):
            if len(vis) ==n:
                self.res.append(''.join(vis))
                return
            v = S[idx]
            if v.lower() in letters:
                dfs(vis+[v.upper()], idx+1)
            dfs(vis+[v.lower()], idx+1)
        dfs([],0)
        return self.res