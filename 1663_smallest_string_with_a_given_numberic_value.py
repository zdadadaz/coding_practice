class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        letters = [chr(i+ord('a')) for i in range(26)]
        if k<25 and n==1:
            return letters[k]      
        res = ['']*n
        for i in range(n-1,-1,-1):
            init = min(26,k-n+1)
            n-=1
            k-=init
            res[i]=letters[init-1]
        return ''.join(res)

