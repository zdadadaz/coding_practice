class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(A,idx): 
            for i in range(0,idx//2+1):
                A[idx-i],A[i] = A[i],A[idx-i]
                
        res = []
        n = len(A)
        while n>0:
            i = 0
            while A[i]!= n:
                i+=1
            if i != 0:
                flip(A,i)
                res.append(i+1)
            flip(A,n-1)
            res.append(n)
            n-=1
        return res