class Solution:
    # O(N)/O(N)
    # Reduce space to O(1)
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.backspaceString(S)
        t = self.backspaceString(T)
        if s == t:
            return True
        else:
            return False
        
    def backspaceString(self,S):
        count = 0
        out = []
        for i in range(len(S)-1,-1,-1):
            if S[i] == "#":
                count += 1
            elif S[i] != "#" and count == 0:
                out.append(S[i])
            elif S[i] != "#" and count != 0:
                count -= 1
                continue    
        return out

    # using pop!!!!!!(stack more generally)
    def backspaceCompare_web(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
    # Slow!! Runtime: 32 ms, faster than 32.41% of Python3 online
    def backspaceCompare_Save_space(self, S: str, T: str) -> bool:
        def backspaceString(S, index, count):
            while index[0]>-1:
                if S[index[0]] == "#":
                    count[0] += 1
                elif S[index[0]] != "#" and count[0] == 0:
                    return S[index[0]]
                elif S[index[0]] != "#" and count[0] != 0:
                    count[0] -= 1
                index[0]-=1
             
        count_s = [0]
        count_t = [0]
        s = [len(S)-1]
        t = [len(T)-1]
        while s[0] > -1 and t[0] >-1:
            out_s=backspaceString(S, s, count_s)
            out_t=backspaceString(T, t, count_t)
            if (out_s != out_t):
                return False
            s[0]-=1
            t[0]-=1
        def countsign(S,s):
            count =0
            if s==0:
                return False
            for i in range(s,-1,-1):
                if S[i] == "#":
                    count += 1
            if count >= int(s/2):
                return True
            else:
                return False
        if s[0]>-1:
            return countsign(S,s[0])
        if t[0] > -1:
            return countsign(S,s[0])
        return True
sol = Solution()
a="bbbextm"
b="bbb#extm"
print(sol.backspaceCompare_Save_space(a,b))