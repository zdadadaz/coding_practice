class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1]-A[0]
        for i in range(len(A)-1):
            mv = min(A[0]+K, A[i+1]-K)
            Mv = max(A[i]+K, A[-1]-K)
            res = min(res, Mv-mv)
        return res
            