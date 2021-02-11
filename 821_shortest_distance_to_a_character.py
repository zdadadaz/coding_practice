class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [float('inf')]*n
        def helper(s, c, res):
            prv = -1
            for i in range(n):
                if s[i] == c:
                    res[i] = 0
                    prv = i
                elif prv != -1:
                    res[i] = min(res[i], i-prv)

        def helper_inverse(s, c, res):
            prv = -1
            for i in range(n-1,-1,-1):
                if s[i] == c:
                    res[i] = 0
                    prv = i
                elif prv != -1:
                    res[i] = min(res[i], prv-i)

        helper(s,c,res)
        helper_inverse(s,c,res)
        
        return res