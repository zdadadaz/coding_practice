class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        an,bn = len(a), len(b)
        prv=0
        i,j=an-1,bn-1
        inum = jnum = None
        while i >-1 or j >-1: 
            inum = int(a[i]) if i > -1 else 0
            jnum = int(b[j]) if j > -1 else 0
            res.append(str((inum+jnum+prv)%2))
            prv = (inum+jnum+prv)//2
            i-=1
            j-=1
        if prv == 1:
            return ''.join([str(1)]+res[::-1])
        return ''.join(res[::-1])