class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        max1 = self.countoverlap(A,B)
        max2 = self.countoverlap(B,A)
        return max(max1, max2)

    def countoverlap(self,A,B):
        maxover = 0
        for x in range(len(A)):
            for y in range(len(A)):
                tmp = 0
                for i in range(len(A)):
                    for j in range(len(A)):
                        if A[i][j]==1:
                            if i-y>=0 and j-x>=0 and i-y<len(A) and j-x<len(A) and B[i-y][j-x]:
                                tmp+=1
                maxover = max(maxover,tmp)
        return maxover
                                